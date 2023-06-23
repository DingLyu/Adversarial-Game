import networkx as nx

# a
def cooperative_attacking(sys1, sys2):
    attack_orders = {}
    Team = {}
    ack_seq = sorted(sys1.G.nodes(), key=lambda i: sys1.node_attr[i]['ACK'] * sys1.node_attr[i]['LS'], reverse=True)
    has_mission = {attacker: False for attacker in sys1.G.nodes()}
    target_seq = sorted(sys2.G.nodes(), key=lambda i: sys2.node_attr[i]['ACK'] * sys2.node_attr[i]['LS'] * sys2.node_attr[i]['DEF'], reverse=True)
    item = 0
    for attacker in ack_seq:
        if not has_mission[attacker]:
            if sys2.node_status[target_seq[item]] != 'destroyed':
                has_mission[attacker] = True
                Target = target_seq[item]
            elif item + 1 < sys2.N:
                item += 1
                has_mission[attacker] = True
                Target = target_seq[item]
            else:
                Target = None
            if Target != None:
                attack_orders[attacker] = {'team': [attacker], 'target': Target}
            else:
                continue
            if sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF'] >= sys2.node_attr[Target]['HP']:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                Team[attacker] = {}
                for coop in sys1.G.predecessors(attacker):
                    if not has_mission[coop]:
                        deltaAttack = (sys1.node_attr[attacker]['LS']) * (sys1.node_attr[coop]['ACK'] - sys1.coop_cost[(coop, attacker)]) \
                                      - sys1.node_attr[coop]['ACK']
                        if deltaAttack > 0:
                            Team[attacker][coop] = deltaAttack
                if Team[attacker]:
                    DMGE = sys1.node_attr[attacker]['LS'] * sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                    Coop = sorted(Team[attacker], key=lambda i: Team[attacker][i], reverse=True)
                    for coop in Coop:
                        DMGE += (sys1.node_attr[attacker]['LS']) * (sys1.node_attr[coop]['ACK'] - sys1.coop_cost[(coop, attacker)]) \
                                - sys2.node_attr[Target]['DEF']
                        attack_orders[attacker]['team'].append(coop)
                        has_mission[coop] = True
                        if DMGE >= sys2.node_attr[Target]['HP']:
                            break
                    if DMGE >= sys2.node_attr[Target]['HP']:
                        sys2.node_attr[Target]['HP'] = 0
                        sys2.node_status[Target] = 'destroyed'
                    else:
                        sys2.node_attr[Target]['HP'] -= DMGE
                        sys2.node_status[Target] = 'under_attack'
                else:
                    sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                    sys2.node_status[Target] = 'under_attack'
    return attack_orders

# b
def cooperative_attacking_degree(sys1, sys2):
    attack_orders = {}
    Team = {}
    ack_seq = sorted(sys1.G.nodes(), key=lambda i: sys1.node_attr[i]['ACK'] * sys1.node_attr[i]['LS'], reverse=True)
    has_mission = {attacker: False for attacker in sys1.G.nodes()}
    node_importance = {node: sys2.G.in_degree(node) for node in sys2.G.nodes()}
    target_seq = sorted(node_importance, key=lambda i: node_importance[i], reverse=True)
    item = 0
    for attacker in ack_seq:
        if not has_mission[attacker]:
            if sys2.node_status[target_seq[item]] != 'destroyed':
                has_mission[attacker] = True
                Target = target_seq[item]
            elif item + 1 < sys2.N:
                item += 1
                has_mission[attacker] = True
                Target = target_seq[item]
            else:
                Target = None
            if Target != None:
                attack_orders[attacker] = {'team': [attacker], 'target': Target}
            else:
                continue
            if sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF'] >= sys2.node_attr[Target]['HP']:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                Team[attacker] = {}
                for coop in sys1.G.predecessors(attacker):
                    if not has_mission[coop]:
                        deltaAttack = (sys1.node_attr[attacker]['LS']) * (sys1.node_attr[coop]['ACK'] - sys1.coop_cost[(coop, attacker)]) \
                                      - sys1.node_attr[coop]['ACK']
                        if deltaAttack > 0:
                            Team[attacker][coop] = deltaAttack
                if Team[attacker]:
                    DMGE = sys1.node_attr[attacker]['LS'] * sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                    Coop = sorted(Team[attacker], key=lambda i: Team[attacker][i], reverse=True)
                    for coop in Coop:
                        DMGE += (sys1.node_attr[attacker]['LS']) * (sys1.node_attr[coop]['ACK'] - sys1.coop_cost[(coop, attacker)]) \
                                - sys2.node_attr[Target]['DEF']
                        attack_orders[attacker]['team'].append(coop)
                        has_mission[coop] = True
                        if DMGE >= sys2.node_attr[Target]['HP']:
                            break
                    if DMGE >= sys2.node_attr[Target]['HP']:
                        sys2.node_attr[Target]['HP'] = 0
                        sys2.node_status[Target] = 'destroyed'
                    else:
                        sys2.node_attr[Target]['HP'] -= DMGE
                        sys2.node_status[Target] = 'under_attack'
                else:
                    sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                    sys2.node_status[Target] = 'under_attack'
    return attack_orders

# c
def cooperative_attacking_clustering(sys1, sys2):
    attack_orders = {}
    Team = {}
    ack_seq = sorted(sys1.G.nodes(), key=lambda i: sys1.node_attr[i]['ACK'] * sys1.node_attr[i]['LS'], reverse=True)
    has_mission = {attacker: False for attacker in sys1.G.nodes()}
    node_importance = nx.clustering(sys2.G)
    target_seq = sorted(node_importance, key=lambda i: node_importance[i], reverse=True)
    item = 0
    for attacker in ack_seq:
        if not has_mission[attacker]:
            if sys2.node_status[target_seq[item]] != 'destroyed':
                has_mission[attacker] = True
                Target = target_seq[item]
            elif item + 1 < sys2.N:
                item += 1
                has_mission[attacker] = True
                Target = target_seq[item]
            else:
                Target = None
            if Target != None:
                attack_orders[attacker] = {'team': [attacker], 'target': Target}
            else:
                continue
            if sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF'] >= sys2.node_attr[Target]['HP']:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                Team[attacker] = {}
                for coop in sys1.G.predecessors(attacker):
                    if not has_mission[coop]:
                        deltaAttack = (sys1.node_attr[attacker]['LS']) * (sys1.node_attr[coop]['ACK'] - sys1.coop_cost[(coop, attacker)]) \
                                      - sys1.node_attr[coop]['ACK']
                        if deltaAttack > 0:
                            Team[attacker][coop] = deltaAttack
                if Team[attacker]:
                    DMGE = sys1.node_attr[attacker]['LS'] * sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                    Coop = sorted(Team[attacker], key=lambda i: Team[attacker][i], reverse=True)
                    for coop in Coop:
                        DMGE += (sys1.node_attr[attacker]['LS']) * (sys1.node_attr[coop]['ACK'] - sys1.coop_cost[(coop, attacker)]) \
                                - sys2.node_attr[Target]['DEF']
                        attack_orders[attacker]['team'].append(coop)
                        has_mission[coop] = True
                        if DMGE >= sys2.node_attr[Target]['HP']:
                            break
                    if DMGE >= sys2.node_attr[Target]['HP']:
                        sys2.node_attr[Target]['HP'] = 0
                        sys2.node_status[Target] = 'destroyed'
                    else:
                        sys2.node_attr[Target]['HP'] -= DMGE
                        sys2.node_status[Target] = 'under_attack'
                else:
                    sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                    sys2.node_status[Target] = 'under_attack'
    return attack_orders

# d
def cooperative_attacking_betweenness(sys1, sys2):
    attack_orders = {}
    Team = {}
    ack_seq = sorted(sys1.G.nodes(), key=lambda i: sys1.node_attr[i]['ACK'] * sys1.node_attr[i]['LS'], reverse=True)
    has_mission = {attacker: False for attacker in sys1.G.nodes()}
    node_importance = nx.betweenness_centrality(sys2.G)
    target_seq = sorted(node_importance, key=lambda i: node_importance[i], reverse=True)
    item = 0
    for attacker in ack_seq:
        if not has_mission[attacker]:
            if sys2.node_status[target_seq[item]] != 'destroyed':
                has_mission[attacker] = True
                Target = target_seq[item]
            elif item + 1 < sys2.N:
                item += 1
                has_mission[attacker] = True
                Target = target_seq[item]
            else:
                Target = None
            if Target != None:
                attack_orders[attacker] = {'team': [attacker], 'target': Target}
            else:
                continue
            if sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF'] >= sys2.node_attr[Target]['HP']:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                Team[attacker] = {}
                for coop in sys1.G.predecessors(attacker):
                    if not has_mission[coop]:
                        deltaAttack = (sys1.node_attr[attacker]['LS']) * (sys1.node_attr[coop]['ACK'] - sys1.coop_cost[(coop, attacker)]) \
                                      - sys1.node_attr[coop]['ACK']
                        if deltaAttack > 0:
                            Team[attacker][coop] = deltaAttack
                if Team[attacker]:
                    DMGE = sys1.node_attr[attacker]['LS'] * sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                    Coop = sorted(Team[attacker], key=lambda i: Team[attacker][i], reverse=True)
                    for coop in Coop:
                        DMGE += (sys1.node_attr[attacker]['LS']) * (sys1.node_attr[coop]['ACK'] - sys1.coop_cost[(coop, attacker)]) \
                                - sys2.node_attr[Target]['DEF']
                        attack_orders[attacker]['team'].append(coop)
                        has_mission[coop] = True
                        if DMGE >= sys2.node_attr[Target]['HP']:
                            break
                    if DMGE >= sys2.node_attr[Target]['HP']:
                        sys2.node_attr[Target]['HP'] = 0
                        sys2.node_status[Target] = 'destroyed'
                    else:
                        sys2.node_attr[Target]['HP'] -= DMGE
                        sys2.node_status[Target] = 'under_attack'
                else:
                    sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                    sys2.node_status[Target] = 'under_attack'
    return attack_orders

# e
def cooperative_attacking_closeness(sys1, sys2):
    attack_orders = {}
    Team = {}
    ack_seq = sorted(sys1.G.nodes(), key=lambda i: sys1.node_attr[i]['ACK'] * sys1.node_attr[i]['LS'], reverse=True)
    has_mission = {attacker: False for attacker in sys1.G.nodes()}
    node_importance = nx.closeness_centrality(sys2.G)
    target_seq = sorted(node_importance, key=lambda i: node_importance[i], reverse=True)
    item = 0
    for attacker in ack_seq:
        if not has_mission[attacker]:
            if sys2.node_status[target_seq[item]] != 'destroyed':
                has_mission[attacker] = True
                Target = target_seq[item]
            elif item + 1 < sys2.N:
                item += 1
                has_mission[attacker] = True
                Target = target_seq[item]
            else:
                Target = None
            if Target != None:
                attack_orders[attacker] = {'team': [attacker], 'target': Target}
            else:
                continue
            if sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF'] >= sys2.node_attr[Target]['HP']:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                Team[attacker] = {}
                for coop in sys1.G.predecessors(attacker):
                    if not has_mission[coop]:
                        deltaAttack = (sys1.node_attr[attacker]['LS']) * (sys1.node_attr[coop]['ACK'] - sys1.coop_cost[(coop, attacker)]) \
                                      - sys1.node_attr[coop]['ACK']
                        if deltaAttack > 0:
                            Team[attacker][coop] = deltaAttack
                if Team[attacker]:
                    DMGE = sys1.node_attr[attacker]['LS'] * sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                    Coop = sorted(Team[attacker], key=lambda i: Team[attacker][i], reverse=True)
                    for coop in Coop:
                        DMGE += (sys1.node_attr[attacker]['LS']) * (sys1.node_attr[coop]['ACK'] - sys1.coop_cost[(coop, attacker)]) \
                                - sys2.node_attr[Target]['DEF']
                        attack_orders[attacker]['team'].append(coop)
                        has_mission[coop] = True
                        if DMGE >= sys2.node_attr[Target]['HP']:
                            break
                    if DMGE >= sys2.node_attr[Target]['HP']:
                        sys2.node_attr[Target]['HP'] = 0
                        sys2.node_status[Target] = 'destroyed'
                    else:
                        sys2.node_attr[Target]['HP'] -= DMGE
                        sys2.node_status[Target] = 'under_attack'
                else:
                    sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                    sys2.node_status[Target] = 'under_attack'
    return attack_orders

