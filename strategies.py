import networkx as nx
from utils import *

def low_DEF_first(sys1, sys2):
    attack_orders = {}
    attackers = {attacker: sys1.node_attr[attacker]['ACK'] for attacker in sys1.G.nodes()}
    attacker_seq = sorted(attackers, key=lambda i: attackers[i], reverse=True)
    accumulative_dmg = {enemy: 0 for enemy in sys2.G.nodes()}
    def_inv = sum([1 / sys2.node_attr[enemy]['DEF'] for enemy in sys2.G.nodes()])
    for enemy in sys2.G.nodes():
        sys2.node_attr[enemy]['r'] = 1 / sys2.node_attr[enemy]['DEF'] / def_inv * sys2.N
    for attacker in attacker_seq:
        Reward = 0
        Target = None
        for enemy in sys2.G.nodes():
            if accumulative_dmg[enemy] < sys2.node_attr[enemy]['HP']:
                dmg = sys1.node_attr[attacker]['ACK'] - sys2.node_attr[enemy]['DEF']
                Expect = dmg / sys2.node_attr[enemy]['HP'] * sys2.node_attr[enemy]['r']
                if Expect > Reward:
                    Reward = Expect
                    Target = enemy
        if Target != None:
            accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            attack_orders[attacker] = {'target': Target}
    return attack_orders, accumulative_dmg

def low_ACK_first(sys1, sys2):
    attack_orders = {}
    attackers = {attacker: sys1.node_attr[attacker]['ACK'] for attacker in sys1.G.nodes()}
    attacker_seq = sorted(attackers, key=lambda i: attackers[i], reverse=True)
    accumulative_dmg = {enemy: 0 for enemy in sys2.G.nodes()}
    ack_inv = sum([1 / sys2.node_attr[enemy]['ACK'] for enemy in sys2.G.nodes()])
    for enemy in sys2.G.nodes():
        sys2.node_attr[enemy]['r'] = 1 / sys2.node_attr[enemy]['ACK'] / ack_inv * sys2.N
    for attacker in attacker_seq:
        Reward = 0
        Target = None
        for enemy in sys2.G.nodes():
            if accumulative_dmg[enemy] < sys2.node_attr[enemy]['HP']:
                dmg = sys1.node_attr[attacker]['ACK'] - sys2.node_attr[enemy]['DEF']
                Expect = dmg / sys2.node_attr[enemy]['HP'] * sys2.node_attr[enemy]['r']
                if Expect > Reward:
                    Reward = Expect
                    Target = enemy
        if Target != None:
            accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            attack_orders[attacker] = {'target': Target}
    return attack_orders, accumulative_dmg

def high_DEF_first(sys1, sys2):
    attack_orders = {}
    attackers = {attacker: sys1.node_attr[attacker]['ACK'] for attacker in sys1.G.nodes()}
    attacker_seq = sorted(attackers, key=lambda i: attackers[i], reverse=True)
    accumulative_dmg = {enemy: 0 for enemy in sys2.G.nodes()}
    def_sum = sum([sys2.node_attr[enemy]['DEF'] for enemy in sys2.G.nodes()])
    for enemy in sys2.G.nodes():
        sys2.node_attr[enemy]['r'] = sys2.node_attr[enemy]['DEF'] / def_sum * sys2.N
    for attacker in attacker_seq:
        Reward = 0
        Target = None
        for enemy in sys2.G.nodes():
            if accumulative_dmg[enemy] < sys2.node_attr[enemy]['HP']:
                dmg = sys1.node_attr[attacker]['ACK'] - sys2.node_attr[enemy]['DEF']
                Expect = dmg / sys2.node_attr[enemy]['HP'] * sys2.node_attr[enemy]['r']
                if Expect > Reward:
                    Reward = Expect
                    Target = enemy
        if Target != None:
            accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            attack_orders[attacker] = {'target': Target}
    return attack_orders, accumulative_dmg

def high_ACK_first(sys1, sys2):
    attack_orders = {}
    attackers = {attacker: sys1.node_attr[attacker]['ACK'] for attacker in sys1.G.nodes()}
    attacker_seq = sorted(attackers, key=lambda i: attackers[i], reverse=True)
    accumulative_dmg = {enemy: 0 for enemy in sys2.G.nodes()}
    ack_sum = sum([sys2.node_attr[enemy]['ACK'] for enemy in sys2.G.nodes()])
    for enemy in sys2.G.nodes():
        sys2.node_attr[enemy]['r'] = sys2.node_attr[enemy]['ACK'] / ack_sum * sys2.N
    for attacker in attacker_seq:
        Reward = 0
        Target = None
        for enemy in sys2.G.nodes():
            if accumulative_dmg[enemy] < sys2.node_attr[enemy]['HP']:
                dmg = sys1.node_attr[attacker]['ACK'] - sys2.node_attr[enemy]['DEF']
                Expect = dmg / sys2.node_attr[enemy]['HP'] * sys2.node_attr[enemy]['r']
                if Expect > Reward:
                    Reward = Expect
                    Target = enemy
        if Target != None:
            accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            attack_orders[attacker] = {'target': Target}
    return attack_orders, accumulative_dmg

def low_DEF_low_ACK_first(sys1, sys2):
    attack_orders = {}
    attackers = {attacker: sys1.node_attr[attacker]['ACK'] for attacker in sys1.G.nodes()}
    attacker_seq = sorted(attackers, key=lambda i: attackers[i], reverse=True)
    accumulative_dmg = {enemy: 0 for enemy in sys2.G.nodes()}
    ack_def_inv = sum([1 / (sys2.node_attr[enemy]['ACK']*sys2.node_attr[enemy]['DEF']) for enemy in sys2.G.nodes()])
    for enemy in sys2.G.nodes():
        sys2.node_attr[enemy]['r'] = 1 / (sys2.node_attr[enemy]['ACK']*sys2.node_attr[enemy]['DEF']) / ack_def_inv * sys2.N
    for attacker in attacker_seq:
        Reward = 0
        Target = None
        for enemy in sys2.G.nodes():
            if accumulative_dmg[enemy] < sys2.node_attr[enemy]['HP']:
                dmg = sys1.node_attr[attacker]['ACK'] - sys2.node_attr[enemy]['DEF']
                Expect = dmg / sys2.node_attr[enemy]['HP'] * sys2.node_attr[enemy]['r']
                if Expect > Reward:
                    Reward = Expect
                    Target = enemy
        if Target != None:
            accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            attack_orders[attacker] = {'target': Target}
    return attack_orders, accumulative_dmg

def low_ACK_high_DEF_first(sys1, sys2):
    attack_orders = {}
    attackers = {attacker: sys1.node_attr[attacker]['ACK'] for attacker in sys1.G.nodes()}
    attacker_seq = sorted(attackers, key=lambda i: attackers[i], reverse=True)
    accumulative_dmg = {enemy: 0 for enemy in sys2.G.nodes()}
    def_sum_ack_inv = sum([sys2.node_attr[enemy]['DEF'] / sys2.node_attr[enemy]['ACK'] for enemy in sys2.G.nodes()])
    for enemy in sys2.G.nodes():
        sys2.node_attr[enemy]['r'] = sys2.node_attr[enemy]['DEF'] / sys2.node_attr[enemy]['ACK'] / def_sum_ack_inv * sys2.N
    for attacker in attacker_seq:
        Reward = 0
        Target = None
        for enemy in sys2.G.nodes():
            if accumulative_dmg[enemy] < sys2.node_attr[enemy]['HP']:
                dmg = sys1.node_attr[attacker]['ACK'] - sys2.node_attr[enemy]['DEF']
                Expect = dmg / sys2.node_attr[enemy]['HP'] * sys2.node_attr[enemy]['r']
                if Expect > Reward:
                    Reward = Expect
                    Target = enemy
        if Target != None:
            accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            attack_orders[attacker] = {'target': Target}
    return attack_orders, accumulative_dmg

def high_ACK_low_DEF_first(sys1, sys2):
    attack_orders = {}
    attackers = {attacker: sys1.node_attr[attacker]['ACK'] for attacker in sys1.G.nodes()}
    attacker_seq = sorted(attackers, key=lambda i: attackers[i], reverse=True)
    accumulative_dmg = {enemy: 0 for enemy in sys2.G.nodes()}
    ack_sum_def_inv = sum([sys2.node_attr[enemy]['ACK']/sys2.node_attr[enemy]['DEF'] for enemy in sys2.G.nodes()])
    for enemy in sys2.G.nodes():
        sys2.node_attr[enemy]['r'] = sys2.node_attr[enemy]['ACK']/sys2.node_attr[enemy]['DEF'] / ack_sum_def_inv * sys2.N
    for attacker in attacker_seq:
        Reward = 0
        Target = None
        for enemy in sys2.G.nodes():
            if accumulative_dmg[enemy] < sys2.node_attr[enemy]['HP']:
                dmg = sys1.node_attr[attacker]['ACK'] - sys2.node_attr[enemy]['DEF']
                Expect = dmg / sys2.node_attr[enemy]['HP'] * sys2.node_attr[enemy]['r']
                if Expect > Reward:
                    Reward = Expect
                    Target = enemy
        if Target != None:
            accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            attack_orders[attacker] = {'target': Target}
    return attack_orders, accumulative_dmg

def high_ACK_high_DEF_first(sys1, sys2):
    attack_orders = {}
    attackers = {attacker: sys1.node_attr[attacker]['ACK'] for attacker in sys1.G.nodes()}
    attacker_seq = sorted(attackers, key=lambda i: attackers[i], reverse=True)
    accumulative_dmg = {enemy: 0 for enemy in sys2.G.nodes()}
    ack_def_sum = sum([sys2.node_attr[enemy]['ACK']*sys2.node_attr[enemy]['DEF'] for enemy in sys2.G.nodes()])
    for enemy in sys2.G.nodes():
        sys2.node_attr[enemy]['r'] = sys2.node_attr[enemy]['ACK']*sys2.node_attr[enemy]['DEF'] / ack_def_sum * sys2.N
    for attacker in attacker_seq:
        Reward = 0
        Target = None
        for enemy in sys2.G.nodes():
            if accumulative_dmg[enemy] < sys2.node_attr[enemy]['HP']:
                dmg = sys1.node_attr[attacker]['ACK'] - sys2.node_attr[enemy]['DEF']
                Expect = dmg / sys2.node_attr[enemy]['HP'] * sys2.node_attr[enemy]['r']
                if Expect > Reward:
                    Reward = Expect
                    Target = enemy
        if Target != None:
            accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            attack_orders[attacker] = {'target': Target}
    return attack_orders, accumulative_dmg


def cooperative_attacking(sys1, sys2):
    attack_orders = {}
    attackers = {attacker: sys1.node_attr[attacker]['ACK'] * sys1.node_attr[attacker]['LS'] for attacker in sys1.G.nodes()}
    attacker_seq = sorted(attackers, key=lambda i: attackers[i], reverse=True)
    has_mission = {attacker: False for attacker in sys1.G.nodes()}
    accumulative_dmg = {enemy: 0 for enemy in sys2.G.nodes()}
    strength = sum([sys2.node_attr[enemy]['ACK'] * sys2.node_attr[enemy]['LS'] / sys2.node_attr[enemy]['DEF']
                    for enemy in sys2.G.nodes()])
    for enemy in sys2.G.nodes():
        sys2.node_attr[enemy]['strength'] = sys2.node_attr[enemy]['ACK'] * sys2.node_attr[enemy]['LS'] \
                                            / sys2.node_attr[enemy]['DEF'] / strength
    for attacker in attacker_seq:
        if not has_mission[attacker]:
            Reward = 0
            Target = None
            for enemy in sys2.G.nodes():
                if accumulative_dmg[enemy] < sys2.node_attr[enemy]['HP']:
                    Expect = sys2.node_attr[enemy]['strength']
                    # dmg = sys1.node_attr[attacker]['ACK'] - sys2.node_attr[enemy]['DEF']
                    # Expect = dmg / sys2.node_attr[enemy]['HP'] * sys2.node_attr[enemy]['strength']
                    if Expect > Reward:
                        Reward = Expect
                        Target = enemy
            if Target != None:
                has_mission[attacker] = True
                if sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF'] + accumulative_dmg[Target] >= sys2.node_attr[Target]['HP']:
                    accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                    attack_orders[attacker] = {'team': [attacker], 'target': Target}
                else:
                    followers = {}
                    team = [attacker]
                    for neighbor in sys1.G.predecessors(attacker):
                        if not has_mission[neighbor]:
                            deltaAttack = (sys1.node_attr[attacker]['LS']) * (
                                    sys1.node_attr[neighbor]['ACK'] - sys1.coop_cost[(neighbor, attacker)]) \
                                          - sys1.node_attr[neighbor]['ACK']
                            if deltaAttack > 0:
                                followers[neighbor] = deltaAttack
                    if followers:
                        team_dmg = sys1.node_attr[attacker]['LS'] * sys1.node_attr[attacker]['ACK'] - \
                                   sys2.node_attr[Target]['DEF']
                        follower_seq = sorted(followers, key=lambda i: followers[i], reverse=True)
                        for follower in follower_seq:
                            team_dmg += (sys1.node_attr[attacker]['LS']) * (
                                    sys1.node_attr[follower]['ACK'] - sys1.coop_cost[(follower, attacker)]) \
                                        - sys2.node_attr[Target]['DEF']
                            team.append(follower)
                            has_mission[follower] = True
                            if team_dmg + accumulative_dmg[Target] > sys2.node_attr[Target]['HP']:
                                break
                        accumulative_dmg[Target] += team_dmg
                        attack_orders[attacker] = {'team': team, 'target': Target}
                    else:
                        accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                        attack_orders[attacker] = {'team': [attacker], 'target': Target}
    return attack_orders, accumulative_dmg


def cooperative_attacking_degree(sys1, sys2):
    attack_orders = {}
    attackers = {attacker: sys1.node_attr[attacker]['ACK'] * sys1.node_attr[attacker]['LS'] for attacker in sys1.G.nodes()}
    attacker_seq = sorted(attackers, key=lambda i: attackers[i], reverse=True)
    has_mission = {attacker: False for attacker in sys1.G.nodes()}
    accumulative_dmg = {enemy: 0 for enemy in sys2.G.nodes()}
    node_importance = {node: sys2.G.in_degree(node) for node in sys2.G.nodes()}
    importance = sum([node_importance[enemy] + 0.01 for enemy in sys2.G.nodes()])
    for enemy in sys2.G.nodes():
        sys2.node_attr[enemy]['importance'] = (node_importance[enemy] + 0.01) / importance
    for attacker in attacker_seq:
        if not has_mission[attacker]:
            Reward = 0
            Target = None
            for enemy in sys2.G.nodes():
                if accumulative_dmg[enemy] < sys2.node_attr[enemy]['HP']:
                    Expect = sys2.node_attr[enemy]['importance']
                    # dmg = sys1.node_attr[attacker]['ACK'] - sys2.node_attr[enemy]['DEF']
                    # Expect = dmg / sys2.node_attr[enemy]['HP'] * sys2.node_attr[enemy]['importance']
                    if Expect > Reward:
                        Reward = Expect
                        Target = enemy
            if Target != None:
                has_mission[attacker] = True
                if sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF'] + accumulative_dmg[Target] >= sys2.node_attr[Target]['HP']:
                    accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                    attack_orders[attacker] = {'team': [attacker], 'target': Target}
                else:
                    followers = {}
                    team = [attacker]
                    for neighbor in sys1.G.predecessors(attacker):
                        if not has_mission[neighbor]:
                            deltaAttack = (sys1.node_attr[attacker]['LS']) * (
                                    sys1.node_attr[neighbor]['ACK'] - sys1.coop_cost[(neighbor, attacker)]) \
                                          - sys1.node_attr[neighbor]['ACK']
                            if deltaAttack > 0:
                                followers[neighbor] = deltaAttack
                    if followers:
                        team_dmg = sys1.node_attr[attacker]['LS'] * sys1.node_attr[attacker]['ACK'] - \
                                   sys2.node_attr[Target]['DEF']
                        follower_seq = sorted(followers, key=lambda i: followers[i], reverse=True)
                        for follower in follower_seq:
                            team_dmg += (sys1.node_attr[attacker]['LS']) * (
                                    sys1.node_attr[follower]['ACK'] - sys1.coop_cost[(follower, attacker)]) \
                                        - sys2.node_attr[Target]['DEF']
                            team.append(follower)
                            has_mission[follower] = True
                            if team_dmg + accumulative_dmg[Target] > sys2.node_attr[Target]['HP']:
                                break
                        accumulative_dmg[Target] += team_dmg
                        attack_orders[attacker] = {'team': team, 'target': Target}
                    else:
                        accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                        attack_orders[attacker] = {'team': [attacker], 'target': Target}
    return attack_orders, accumulative_dmg


def cooperative_attacking_clustering(sys1, sys2):
    attack_orders = {}
    attackers = {attacker: sys1.node_attr[attacker]['ACK'] * sys1.node_attr[attacker]['LS'] for attacker in
                 sys1.G.nodes()}
    attacker_seq = sorted(attackers, key=lambda i: attackers[i], reverse=True)
    has_mission = {attacker: False for attacker in sys1.G.nodes()}
    accumulative_dmg = {enemy: 0 for enemy in sys2.G.nodes()}
    node_importance = nx.clustering(sys2.G)
    importance = sum([node_importance[enemy] + 0.01 for enemy in sys2.G.nodes()])
    for enemy in sys2.G.nodes():
        sys2.node_attr[enemy]['importance'] = (node_importance[enemy] + 0.01) / importance
    for attacker in attacker_seq:
        if not has_mission[attacker]:
            Reward = 0
            Target = None
            for enemy in sys2.G.nodes():
                if accumulative_dmg[enemy] < sys2.node_attr[enemy]['HP']:
                    Expect = sys2.node_attr[enemy]['importance']
                    # dmg = sys1.node_attr[attacker]['ACK'] - sys2.node_attr[enemy]['DEF']
                    # Expect = dmg / sys2.node_attr[enemy]['HP'] * sys2.node_attr[enemy]['importance']
                    if Expect > Reward:
                        Reward = Expect
                        Target = enemy
            if Target != None:
                has_mission[attacker] = True
                if sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF'] + accumulative_dmg[Target] >= \
                        sys2.node_attr[Target]['HP']:
                    accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                    attack_orders[attacker] = {'team': [attacker], 'target': Target}
                else:
                    followers = {}
                    team = [attacker]
                    for neighbor in sys1.G.predecessors(attacker):
                        if not has_mission[neighbor]:
                            deltaAttack = (sys1.node_attr[attacker]['LS']) * (
                                    sys1.node_attr[neighbor]['ACK'] - sys1.coop_cost[(neighbor, attacker)]) \
                                          - sys1.node_attr[neighbor]['ACK']
                            if deltaAttack > 0:
                                followers[neighbor] = deltaAttack
                    if followers:
                        team_dmg = sys1.node_attr[attacker]['LS'] * sys1.node_attr[attacker]['ACK'] - \
                                   sys2.node_attr[Target]['DEF']
                        follower_seq = sorted(followers, key=lambda i: followers[i], reverse=True)
                        for follower in follower_seq:
                            team_dmg += (sys1.node_attr[attacker]['LS']) * (
                                    sys1.node_attr[follower]['ACK'] - sys1.coop_cost[(follower, attacker)]) \
                                        - sys2.node_attr[Target]['DEF']
                            team.append(follower)
                            has_mission[follower] = True
                            if team_dmg + accumulative_dmg[Target] > sys2.node_attr[Target]['HP']:
                                break
                        accumulative_dmg[Target] += team_dmg
                        attack_orders[attacker] = {'team': team, 'target': Target}
                    else:
                        accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                        attack_orders[attacker] = {'team': [attacker], 'target': Target}
    return attack_orders, accumulative_dmg



def cooperative_attacking_betweenness(sys1, sys2):
    attack_orders = {}
    attackers = {attacker: sys1.node_attr[attacker]['ACK'] * sys1.node_attr[attacker]['LS'] for attacker in
                 sys1.G.nodes()}
    attacker_seq = sorted(attackers, key=lambda i: attackers[i], reverse=True)
    has_mission = {attacker: False for attacker in sys1.G.nodes()}
    accumulative_dmg = {enemy: 0 for enemy in sys2.G.nodes()}
    node_importance = nx.betweenness_centrality(sys2.G)
    importance = sum([node_importance[enemy] + 0.01 for enemy in sys2.G.nodes()])
    for enemy in sys2.G.nodes():
        sys2.node_attr[enemy]['importance'] = (node_importance[enemy] + 0.01) / importance
    for attacker in attacker_seq:
        if not has_mission[attacker]:
            Reward = 0
            Target = None
            for enemy in sys2.G.nodes():
                if accumulative_dmg[enemy] < sys2.node_attr[enemy]['HP']:
                    Expect = sys2.node_attr[enemy]['importance']
                    # dmg = sys1.node_attr[attacker]['ACK'] - sys2.node_attr[enemy]['DEF']
                    # Expect = dmg / sys2.node_attr[enemy]['HP'] * sys2.node_attr[enemy]['importance']
                    if Expect > Reward:
                        Reward = Expect
                        Target = enemy
            if Target != None:
                has_mission[attacker] = True
                if sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF'] + accumulative_dmg[Target] >= \
                        sys2.node_attr[Target]['HP']:
                    accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                    attack_orders[attacker] = {'team': [attacker], 'target': Target}
                else:
                    followers = {}
                    team = [attacker]
                    for neighbor in sys1.G.predecessors(attacker):
                        if not has_mission[neighbor]:
                            deltaAttack = (sys1.node_attr[attacker]['LS']) * (
                                    sys1.node_attr[neighbor]['ACK'] - sys1.coop_cost[(neighbor, attacker)]) \
                                          - sys1.node_attr[neighbor]['ACK']
                            if deltaAttack > 0:
                                followers[neighbor] = deltaAttack
                    if followers:
                        team_dmg = sys1.node_attr[attacker]['LS'] * sys1.node_attr[attacker]['ACK'] - \
                                   sys2.node_attr[Target]['DEF']
                        follower_seq = sorted(followers, key=lambda i: followers[i], reverse=True)
                        for follower in follower_seq:
                            team_dmg += (sys1.node_attr[attacker]['LS']) * (
                                    sys1.node_attr[follower]['ACK'] - sys1.coop_cost[(follower, attacker)]) \
                                        - sys2.node_attr[Target]['DEF']
                            team.append(follower)
                            has_mission[follower] = True
                            if team_dmg + accumulative_dmg[Target] > sys2.node_attr[Target]['HP']:
                                break
                        accumulative_dmg[Target] += team_dmg
                        attack_orders[attacker] = {'team': team, 'target': Target}
                    else:
                        accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                        attack_orders[attacker] = {'team': [attacker], 'target': Target}
    return attack_orders, accumulative_dmg

def cooperative_attacking_closeness(sys1, sys2):
    attack_orders = {}
    attackers = {attacker: sys1.node_attr[attacker]['ACK'] * sys1.node_attr[attacker]['LS'] for attacker in
                 sys1.G.nodes()}
    attacker_seq = sorted(attackers, key=lambda i: attackers[i], reverse=True)
    has_mission = {attacker: False for attacker in sys1.G.nodes()}
    accumulative_dmg = {enemy: 0 for enemy in sys2.G.nodes()}
    node_importance = nx.closeness_centrality(sys2.G)
    importance = sum([node_importance[enemy] + 0.01 for enemy in sys2.G.nodes()])
    for enemy in sys2.G.nodes():
        sys2.node_attr[enemy]['importance'] = (node_importance[enemy] + 0.01) / importance
    for attacker in attacker_seq:
        if not has_mission[attacker]:
            Reward = 0
            Target = None
            for enemy in sys2.G.nodes():
                if accumulative_dmg[enemy] < sys2.node_attr[enemy]['HP']:
                    Expect = sys2.node_attr[enemy]['importance']
                    # dmg = sys1.node_attr[attacker]['ACK'] - sys2.node_attr[enemy]['DEF']
                    # Expect = dmg / sys2.node_attr[enemy]['HP'] * sys2.node_attr[enemy]['importance']
                    if Expect > Reward:
                        Reward = Expect
                        Target = enemy
            if Target != None:
                has_mission[attacker] = True
                if sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF'] + accumulative_dmg[Target] >= \
                        sys2.node_attr[Target]['HP']:
                    accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                    attack_orders[attacker] = {'team': [attacker], 'target': Target}
                else:
                    followers = {}
                    team = [attacker]
                    for neighbor in sys1.G.predecessors(attacker):
                        if not has_mission[neighbor]:
                            deltaAttack = (sys1.node_attr[attacker]['LS']) * (
                                    sys1.node_attr[neighbor]['ACK'] - sys1.coop_cost[(neighbor, attacker)]) \
                                          - sys1.node_attr[neighbor]['ACK']
                            if deltaAttack > 0:
                                followers[neighbor] = deltaAttack
                    if followers:
                        team_dmg = sys1.node_attr[attacker]['LS'] * sys1.node_attr[attacker]['ACK'] - \
                                   sys2.node_attr[Target]['DEF']
                        follower_seq = sorted(followers, key=lambda i: followers[i], reverse=True)
                        for follower in follower_seq:
                            team_dmg += (sys1.node_attr[attacker]['LS']) * (
                                    sys1.node_attr[follower]['ACK'] - sys1.coop_cost[(follower, attacker)]) \
                                        - sys2.node_attr[Target]['DEF']
                            team.append(follower)
                            has_mission[follower] = True
                            if team_dmg + accumulative_dmg[Target] > sys2.node_attr[Target]['HP']:
                                break
                        accumulative_dmg[Target] += team_dmg
                        attack_orders[attacker] = {'team': team, 'target': Target}
                    else:
                        accumulative_dmg[Target] += sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
                        attack_orders[attacker] = {'team': [attacker], 'target': Target}
    return attack_orders, accumulative_dmg



def update_systems(sys1, sys2, accumulative_dmg1, accumulative_dmg2):
    for node in sys1.G.nodes():
        if accumulative_dmg2[node] > 0:
            sys1.node_status[node] = 'under_attack'
        sys1.node_attr[node]['HP'] -= accumulative_dmg2[node]
        if sys1.node_attr[node]['HP'] <= 0:
            sys1.node_status[node] = 'destroyed'
    for node in sys2.G.nodes():
        if accumulative_dmg1[node] > 0:
            sys2.node_status[node] = 'under_attack'
        sys2.node_attr[node]['HP'] -= accumulative_dmg1[node]
        if sys2.node_attr[node]['HP'] <= 0:
            sys2.node_status[node] = 'destroyed'
    sys1._update_system()
    sys2._update_system()


def update_systems_for_visualization(sys1, sys2, accumulative_dmg1, accumulative_dmg2):
    for node in sys1.G.nodes():
        if accumulative_dmg2[node] > 0:
            sys1.node_status[node] = 'under_attack'
        sys1.node_attr[node]['HP'] -= accumulative_dmg2[node]
        if sys1.node_attr[node]['HP'] <= 0:
            sys1.node_status[node] = 'destroyed'
    for node in sys2.G.nodes():
        if accumulative_dmg1[node] > 0:
            sys2.node_status[node] = 'under_attack'
        sys2.node_attr[node]['HP'] -= accumulative_dmg1[node]
        if sys2.node_attr[node]['HP'] <= 0:
            sys2.node_status[node] = 'destroyed'