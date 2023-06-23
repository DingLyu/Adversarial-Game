import networkx as nx

from netsys import *
from utils import *
from withoutcoop_confrontation_strategy import *
from strategies import *

def tracker(sys1, sys2):
    sys1._update_system()
    sys2._update_system()
    sum_ACK_1 ,sum_ACK_2, sum_DEF_1, sum_DEF_2, sum_HP_1, sum_HP_2 = 0, 0, 0, 0, 0, 0
    for node in sys1.G.nodes():
        sum_ACK_1 += sys1.node_attr[node]['ACK']
        sum_DEF_1 += sys1.node_attr[node]['DEF']
        sum_HP_1 += sys1.node_attr[node]['HP']
    for node in sys2.G.nodes():
        sum_ACK_2 += sys2.node_attr[node]['ACK']
        sum_DEF_2 += sys2.node_attr[node]['DEF']
        sum_HP_2 += sys2.node_attr[node]['HP']
    return nx.number_of_nodes(sys1.G), nx.number_of_nodes(sys2.G), sum_ACK_1 ,sum_ACK_2, sum_DEF_1, sum_DEF_2, sum_HP_1, sum_HP_2


def trajectory():
    sys1, sys2 = adversarial_systems_ws(N=1000, num_neighbors=4, p1=0.1, p2=0.1)
    Sys1, Sys2 = copy.deepcopy(sys1), copy.deepcopy(sys2)

    round = 0
    X = [round]
    n1, n2, sum_ACK_1 ,sum_ACK_2, sum_DEF_1, sum_DEF_2, sum_HP_1, sum_HP_2 = tracker(sys1, sys2)
    Y = [[n1, n2, sum_ACK_1 ,sum_ACK_2, sum_DEF_1, sum_DEF_2, sum_HP_1, sum_HP_2]]
    while sys1.G.nodes() and sys2.G.nodes():
        round += 1
        X.append(round)
        AttackingOrders1 = high_ACK_attacking(sys1, sys2)
        AttackingOrders2 = low_DEF_attacking(sys2, sys1)
        n1, n2, sum_ACK_1 ,sum_ACK_2, sum_DEF_1, sum_DEF_2, sum_HP_1, sum_HP_2 = tracker(sys1, sys2)
        Y.append([n1, n2, sum_ACK_1 ,sum_ACK_2, sum_DEF_1, sum_DEF_2, sum_HP_1, sum_HP_2])
    Y = np.array(Y).T
    fig = plt.figure(figsize=(7,7))
    plt.subplot(411)
    # plt.title('high_$ack$_attacking VS low_$def$_attacking')
    plt.scatter(X, Y[0], marker='^', label='$G_1$')
    plt.scatter(X, Y[1], marker='v', label='$G_2$')
    plt.ylabel('$N$', fontsize=20)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(loc='upper right')
    plt.subplot(412)
    plt.scatter(X, Y[2], marker='^', label='$G_1$')
    plt.scatter(X, Y[3], marker='v', label='$G_2$')
    plt.ylabel('sum($ack$)', fontsize=20)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(loc='upper right')
    plt.subplot(413)
    plt.scatter(X, Y[4], marker='^', label='$G_1$')
    plt.scatter(X, Y[5], marker='v', label='$G_2$')
    plt.ylabel('sum($def$)', fontsize=20)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(loc='upper right')
    plt.subplot(414)
    plt.scatter(X, Y[6], marker='^', label='$G_1$')
    plt.scatter(X, Y[7], marker='v', label='$G_2$')
    plt.ylabel('sum($hp$)', fontsize=20)
    plt.xlabel('$t$', fontsize=20)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(loc='upper right')
    plt.subplots_adjust(left=0.16, right=0.98, top=0.98, bottom=0.1)
    fig.align_labels()
    plt.savefig('figs/trajectory.pdf')

def attacking_orders():
    sys1, sys2 = adversarial_systems_ws_powerlaw()
    print(nx.number_of_edges(sys1.G))
    print(nx.number_of_edges(sys2.G))
    attack_orders1, accumulative_dmg1 = cooperative_attacking(sys1, sys2)
    for edge in sys1.G.edges():
        sys1.G[edge[0]][edge[1]]['weight'] = 0.5
    for attacker in attack_orders1:
        for coop in attack_orders1[attacker]['team']:
            if coop != attacker:
                sys1.G[attacker][coop]['weight'] = 2
                sys1.G[coop][attacker]['weight'] = 2
    attack_orders2, accumulative_dmg2 = cooperative_attacking(sys2, sys1)
    for edge in sys2.G.edges():
        sys2.G[edge[0]][edge[1]]['weight'] = 0.5
    for attacker in attack_orders2:
        for coop in attack_orders2[attacker]['team']:
            if coop != attacker:
                sys2.G[attacker][coop]['weight'] = 2
                sys2.G[coop][attacker]['weight'] = 2
    pos1 = forceatlas2.forceatlas2_networkx_layout(G=sys1.G, pos=nx.kamada_kawai_layout(sys1.G), iterations=100)
    pos2 = forceatlas2.forceatlas2_networkx_layout(G=sys2.G, pos=nx.kamada_kawai_layout(sys2.G), iterations=100)
    update_systems_for_visualization(sys1, sys2, accumulative_dmg1, accumulative_dmg2)
    G = nx.DiGraph()
    NODECOLOR = []
    for node in sys1.G.nodes():
        G.add_node(sys1.system_name + str(node))
        NODECOLOR.append(palette['sys1'][sys1.node_status[node]])
    for node in sys2.G.nodes():
        G.add_node(sys2.system_name + str(node))
        NODECOLOR.append(palette['sys2'][sys2.node_status[node]])
    for edge in sys1.G.edges():
        if sys1.node_status[edge[0]] == 'destroyed' or sys1.node_status[edge[1]] == 'destroyed':
            G.add_edge(sys1.system_name + str(edge[0]), sys1.system_name + str(edge[1]),
                       weight=sys1.coop_cost[edge], color=palette['sys1']['destroyed'], width=0.1)
        else:
            G.add_edge(sys1.system_name + str(edge[0]), sys1.system_name + str(edge[1]),
                       weight=sys1.coop_cost[edge], color='black', width=0.1)
    for edge in sys2.G.edges():
        if sys2.node_status[edge[0]] == 'destroyed' or sys2.node_status[edge[1]] == 'destroyed':
            G.add_edge(sys2.system_name + str(edge[0]), sys2.system_name + str(edge[1]),
                       weight=sys2.coop_cost[edge], color=palette['sys2']['destroyed'], width=0.1)
        else:
            G.add_edge(sys2.system_name + str(edge[0]), sys2.system_name + str(edge[1]),
                       weight=sys2.coop_cost[edge], color='black', width=0.1)
    for attacker in attack_orders1:
        if attack_orders1[attacker]['team']:
            for coop in attack_orders1[attacker]['team']:
                if coop != attacker:
                    G.add_edge(sys1.system_name + str(coop), sys1.system_name + str(attacker),
                               color=palette['sys1']['active'], width=1)
        G.add_edge(sys1.system_name + str(attacker), sys2.system_name + str(attack_orders1[attacker]['target']),
                   color=palette['sys1']['active'], width=3)
    for attacker in attack_orders2:
        if attack_orders2[attacker]['team']:
            for coop in attack_orders2[attacker]['team']:
                if coop != attacker:
                    G.add_edge(sys2.system_name + str(coop), sys2.system_name + str(attacker),
                               color=palette['sys2']['active'], width=1)
        G.add_edge(sys2.system_name + str(attacker), sys1.system_name + str(attack_orders2[attacker]['target']),
                   color=palette['sys2']['active'], width=3)
    pos = {}
    for node in pos1:
        pos[sys1.system_name + str(node)] = pos1[node] - np.array([45, 0])
    for node in pos2:
        pos[sys2.system_name + str(node)] = pos2[node] + np.array([45, 0])

    plt.figure(figsize=(10, 6))
    colors = [G[u][v]['color'] for u, v in G.edges()]
    widths = [G[u][v]['width'] for u, v in G.edges()]
    nx.draw(G, node_color=NODECOLOR, node_size=600, edge_color=colors, width=widths, with_labels=True, pos=pos, font_color='white')
    plt.savefig('figs/attack_orders.png')
    plt.show()


def target_selection():
    sys1, sys2 = adversarial_systems_ws()
    pos2 = forceatlas2.forceatlas2_networkx_layout(G=sys2.G, pos=nx.kamada_kawai_layout(sys2.G), iterations=100)
    X, Y = [], []
    for key in pos2:
        X.append(pos2[key][0])
        Y.append(pos2[key][1])
    x, y = min(X), max(Y)+3
    for dim in range(4):
        target_selection_node_importance(copy.deepcopy(sys1), copy.deepcopy(sys2), pos2, dim, x, y)


def target_selection_node_importance(sys1, sys2, pos2, dim, x, y):
    if dim == 0:
        attack_orders1, accumulative_dmg1 = cooperative_attacking_degree(sys1, sys2)
    if dim == 1:
        attack_orders1, accumulative_dmg1 = cooperative_attacking_betweenness(sys1, sys2)
    if dim == 2:
        attack_orders1, accumulative_dmg1 = cooperative_attacking_closeness(sys1, sys2)
    if dim == 3:
        attack_orders1, accumulative_dmg1 = cooperative_attacking_clustering(sys1, sys2)
    attack_orders2, accumulative_dmg2 = cooperative_attacking(sys2, sys1)
    update_systems_for_visualization(sys1, sys2, accumulative_dmg1, accumulative_dmg2)
    G = nx.DiGraph()
    NODECOLOR = []
    labeldict = {}
    filename = ['figs/target_selection_ccs_k.pdf', 'figs/target_selection_ccs_bet.pdf', 'figs/target_selection_ccs_clo.pdf', 'figs/target_selection_ccs_clu.pdf']
    labelname = ['$k^{in}$', '$bet$', '$clo$', '$clu$']
    for node in sys2.G.nodes():
        G.add_node(sys2.system_name + str(node))
        NODECOLOR.append(palette['sys2'][sys2.node_status[node]])
        labeldict[sys2.system_name + str(node)] = [sys2.G.in_degree(node),nx.betweenness_centrality(sys2.G)[node],
                                                   nx.closeness_centrality(sys2.G)[node], nx.clustering(sys2.G)[node]]
    for edge in sys2.G.edges():
        if sys2.node_status[edge[0]] == 'destroyed' or sys2.node_status[edge[1]] == 'destroyed':
            G.add_edge(sys2.system_name + str(edge[0]), sys2.system_name + str(edge[1]),
                       weight=sys2.coop_cost[edge], color=palette['sys2']['destroyed'], width=0.1)
        else:
            G.add_edge(sys2.system_name + str(edge[0]), sys2.system_name + str(edge[1]),
                       weight=sys2.coop_cost[edge], color='black', width=0.1)
    pos = {}
    for node in pos2:
        pos[sys2.system_name + str(node)] = pos2[node]
    plt.figure(figsize=(6, 6))
    colors = [G[u][v]['color'] for u, v in G.edges()]
    widths = [G[u][v]['width'] for u, v in G.edges()]
    nx.draw(G, node_color=NODECOLOR, node_size=600, edge_color=colors, width=widths, with_labels=True, pos=pos,
            font_color='white')
    for node in pos:
        plt.text(pos[node][0] + 0.02, pos[node][1], labelname[dim] + '=' + str(round(labeldict[node][dim], 2)),
                 fontsize=10)
    plt.text(x, y, 'WS small-world network', fontsize=20)
    plt.savefig(filename[dim])


def gif():
    duration = 50
    sys1, sys2 = adversarial_systems_ws_powerlaw()
    pos1 = forceatlas2.forceatlas2_networkx_layout(G=sys1.G, pos=nx.kamada_kawai_layout(sys1.G), iterations=100)
    pos2 = forceatlas2.forceatlas2_networkx_layout(G=sys2.G, pos=nx.kamada_kawai_layout(sys2.G), iterations=100)

    def compute_layout(sys1, sys2, pos1, pos2):
        attack_orders1, accumulative_dmg1 = cooperative_attacking(sys1, sys2)
        for edge in sys1.G.edges():
            sys1.G[edge[0]][edge[1]]['weight'] = 0.5
        for attacker in attack_orders1:
            for coop in attack_orders1[attacker]['team']:
                if coop != attacker:
                    sys1.G[attacker][coop]['weight'] = 2
                    sys1.G[coop][attacker]['weight'] = 2
        attack_orders2, accumulative_dmg2 = cooperative_attacking(sys2, sys1)
        for edge in sys2.G.edges():
            sys2.G[edge[0]][edge[1]]['weight'] = 0.5
        for attacker in attack_orders2:
            for coop in attack_orders2[attacker]['team']:
                if coop != attacker:
                    sys2.G[attacker][coop]['weight'] = 2
                    sys2.G[coop][attacker]['weight'] = 2
        pos1 = forceatlas2.forceatlas2_networkx_layout(G=sys1.G, pos=pos1, iterations=100)
        pos2 = forceatlas2.forceatlas2_networkx_layout(G=sys2.G, pos=pos2, iterations=100)
        return pos1, pos2

    def noattack(sys1, sys2, pos1, pos2):
        pos1 = forceatlas2.forceatlas2_networkx_layout(G=sys1.G, pos=pos1, iterations=1)
        pos2 = forceatlas2.forceatlas2_networkx_layout(G=sys2.G, pos=pos2, iterations=1)
        G = nx.DiGraph()
        NODECOLOR = []
        for node in sys1.G.nodes():
            G.add_node(sys1.system_name + str(node))
            NODECOLOR.append(palette['sys1'][sys1.node_status[node]])
        for node in sys2.G.nodes():
            G.add_node(sys2.system_name + str(node))
            NODECOLOR.append(palette['sys2'][sys2.node_status[node]])
        for edge in sys1.G.edges():
            G.add_edge(sys1.system_name + str(edge[0]), sys1.system_name + str(edge[1]),
                           weight=sys1.coop_cost[edge], color='black', width=0.1)
        for edge in sys2.G.edges():
            G.add_edge(sys2.system_name + str(edge[0]), sys2.system_name + str(edge[1]),
                           weight=sys2.coop_cost[edge], color='black', width=0.1)
        pos = {}
        for node in pos1:
            pos[sys1.system_name + str(node)] = pos1[node] - np.array([45, 0])
        for node in pos2:
            pos[sys2.system_name + str(node)] = pos2[node] + np.array([45, 0])

        colors = [G[u][v]['color'] for u, v in G.edges()]
        widths = [G[u][v]['width'] for u, v in G.edges()]

        nx.draw(G, node_color=NODECOLOR, edge_color=colors, width=widths, with_labels=True, pos=pos)

    def coop(sys1, sys2, pos1, pos2):
        attack_orders1, accumulative_dmg1 = cooperative_attacking(sys1, sys2)
        attack_orders2, accumulative_dmg2 = cooperative_attacking(sys2, sys1)
        pos1, pos2 = compute_layout(sys1, sys2, pos1, pos2)
        G = nx.DiGraph()
        NODECOLOR = []
        for node in sys1.G.nodes():
            G.add_node(sys1.system_name + str(node))
            NODECOLOR.append(palette['sys1'][sys1.node_status[node]])
        for node in sys2.G.nodes():
            G.add_node(sys2.system_name + str(node))
            NODECOLOR.append(palette['sys2'][sys2.node_status[node]])
        for edge in sys1.G.edges():
            G.add_edge(sys1.system_name + str(edge[0]), sys1.system_name + str(edge[1]),
                           weight=sys1.coop_cost[edge], color='black', width=0.1)
        for edge in sys2.G.edges():
            G.add_edge(sys2.system_name + str(edge[0]), sys2.system_name + str(edge[1]),
                           weight=sys2.coop_cost[edge], color='black', width=0.1)
        for attacker in attack_orders1:
            if attack_orders1[attacker]['team']:
                for coop in attack_orders1[attacker]['team']:
                    if coop != attacker:
                        G.add_edge(sys1.system_name + str(coop), sys1.system_name + str(attacker),
                                   color=palette['sys1']['active'], width=3)
        for attacker in attack_orders2:
            if attack_orders2[attacker]['team']:
                for coop in attack_orders2[attacker]['team']:
                    if coop != attacker:
                        G.add_edge(sys2.system_name + str(coop), sys2.system_name + str(attacker),
                               color=palette['sys2']['active'], width=3)
        pos = {}
        for node in pos1:
            pos[sys1.system_name + str(node)] = pos1[node] - np.array([45, 0])
        for node in pos2:
            pos[sys2.system_name + str(node)] = pos2[node] + np.array([45, 0])

        colors = [G[u][v]['color'] for u, v in G.edges()]
        widths = [G[u][v]['width'] for u, v in G.edges()]
        nx.draw(G, node_color=NODECOLOR, edge_color=colors, width=widths, with_labels=True, pos=pos)

    def attack(sys1, sys2, pos1, pos2):
        attack_orders1, accumulative_dmg1 = cooperative_attacking(sys1, sys2)
        attack_orders2, accumulative_dmg2 = cooperative_attacking(sys2, sys1)
        pos1, pos2 = compute_layout(sys1, sys2, pos1, pos2)
        update_systems_for_visualization(sys1, sys2, accumulative_dmg1, accumulative_dmg2)
        G = nx.DiGraph()
        NODECOLOR = []
        for node in sys1.G.nodes():
            G.add_node(sys1.system_name + str(node))
            NODECOLOR.append(palette['sys1'][sys1.node_status[node]])
        for node in sys2.G.nodes():
            G.add_node(sys2.system_name + str(node))
            NODECOLOR.append(palette['sys2'][sys2.node_status[node]])
        for edge in sys1.G.edges():
            if sys1.node_status[edge[0]] == 'destroyed' or sys1.node_status[edge[1]] == 'destroyed':
                G.add_edge(sys1.system_name + str(edge[0]), sys1.system_name + str(edge[1]),
                           weight=sys1.coop_cost[edge], color=palette['sys1']['destroyed'], width=0.1)
            else:
                G.add_edge(sys1.system_name + str(edge[0]), sys1.system_name + str(edge[1]),
                           weight=sys1.coop_cost[edge], color='black', width=0.1)
        for edge in sys2.G.edges():
            if sys2.node_status[edge[0]] == 'destroyed' or sys2.node_status[edge[1]] == 'destroyed':
                G.add_edge(sys2.system_name + str(edge[0]), sys2.system_name + str(edge[1]),
                           weight=sys2.coop_cost[edge], color=palette['sys2']['destroyed'], width=0.1)
            else:
                G.add_edge(sys2.system_name + str(edge[0]), sys2.system_name + str(edge[1]),
                           weight=sys2.coop_cost[edge], color='black', width=0.1)
        for attacker in attack_orders1:
            if attack_orders1[attacker]['team']:
                for coop in attack_orders1[attacker]['team']:
                    if coop != attacker:
                        G.add_edge(sys1.system_name + str(coop), sys1.system_name + str(attacker),
                               color=palette['sys1']['active'], width=3)
            G.add_edge(sys1.system_name + str(attacker), sys2.system_name + str(attack_orders1[attacker]['target']),
                       color=palette['sys1']['active'], width=3)
        for attacker in attack_orders2:
            if attack_orders2[attacker]['team']:
                for coop in attack_orders2[attacker]['team']:
                    if coop != attacker:
                        G.add_edge(sys2.system_name + str(coop), sys2.system_name + str(attacker),
                               color=palette['sys2']['active'], width=3)
            G.add_edge(sys2.system_name + str(attacker), sys1.system_name + str(attack_orders2[attacker]['target']),
                       color=palette['sys2']['active'], width=3)
        pos = {}
        for node in pos1:
            pos[sys1.system_name + str(node)] = pos1[node] - np.array([45, 0])
        for node in pos2:
            pos[sys2.system_name + str(node)] = pos2[node] + np.array([45, 0])

        colors = [G[u][v]['color'] for u, v in G.edges()]
        widths = [G[u][v]['width'] for u, v in G.edges()]

        nx.draw(G, node_color=NODECOLOR, edge_color=colors, width=widths, with_labels=True, pos=pos)

    def update(sys1, sys2, pos1, pos2):
        sys1._update_system()
        sys2._update_system()
        pos1 = forceatlas2.forceatlas2_networkx_layout(G=sys1.G, pos=pos1, iterations=1)
        pos2 = forceatlas2.forceatlas2_networkx_layout(G=sys2.G, pos=pos2, iterations=1)
        G = nx.DiGraph()
        NODECOLOR = []
        for node in sys1.G.nodes():
            G.add_node(sys1.system_name + str(node))
            NODECOLOR.append(palette['sys1'][sys1.node_status[node]])
        for node in sys2.G.nodes():
            G.add_node(sys2.system_name + str(node))
            NODECOLOR.append(palette['sys2'][sys2.node_status[node]])
        for edge in sys1.G.edges():
            G.add_edge(sys1.system_name + str(edge[0]), sys1.system_name + str(edge[1]),
                       weight=sys1.coop_cost[edge], color='black', width=0.1)
        for edge in sys2.G.edges():
            G.add_edge(sys2.system_name + str(edge[0]), sys2.system_name + str(edge[1]),
                       weight=sys2.coop_cost[edge], color='black', width=0.1)
        pos = {}
        for node in pos1:
            pos[sys1.system_name + str(node)] = pos1[node] - np.array([45, 0])
        for node in pos2:
            pos[sys2.system_name + str(node)] = pos2[node] + np.array([45, 0])

        colors = [G[u][v]['color'] for u, v in G.edges()]
        widths = [G[u][v]['width'] for u, v in G.edges()]

        nx.draw(G, node_color=NODECOLOR, edge_color=colors, width=widths, with_labels=True, pos=pos)

    def make_frame_mpl(t):
        fig = plt.figure(figsize=(10, 6))
        try:
            if int(5 * t) % 5 < 1:
                noattack(sys1, sys2, pos1, pos2)
            if int(5 * t) % 5 == 1:
                coop(sys1, sys2, pos1, pos2)
            if int(5 * t) % 5 == 2:
                attack(sys1, sys2, pos1, pos2)
            if int(5 * t) % 5 >= 3:
                update(sys1, sys2, pos1, pos2)
        except:
            if not sys1.G.nodes() and not sys2.G.nodes():
                res = 'tie!'
            elif not sys1.G.nodes():
                res = 'Net II wins!'
            elif not sys2.G.nodes():
                res = 'Net I wins!'
            plt.axis('off')
            plt.text(x=.5, y=.5, s=res, fontsize=20, verticalalignment="center", horizontalalignment="center")
        return mplfig_to_npimage(fig)

    animation = mpy.VideoClip(make_frame_mpl, duration=duration)
    animation.write_gif("figs/demo.gif", fps=5)

