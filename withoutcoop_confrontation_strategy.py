# 1
def low_DEF_attacking(sys1, sys2):
    attack_orders = {}
    ack_seq = sorted(sys1.G.nodes(), key=lambda i:sys1.node_attr[i]['ACK'], reverse=True)
    target_seq = sorted(sys2.G.nodes(), key=lambda i: sys2.node_attr[i]['DEF'], reverse=False)
    item = 0
    for attacker in ack_seq:
        if sys2.node_status[target_seq[item]] != 'destroyed':
            Target = target_seq[item]
            attack_orders[attacker] = {'team': [attacker], 'target': Target}
            sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            if sys2.node_attr[Target]['HP'] <= 0:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                sys2.node_status[Target] = 'under_attack'
        elif item+1 < sys2.N:
            item += 1
            Target = target_seq[item]
            attack_orders[attacker] = {'team': [attacker], 'target': Target}
            sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            if sys2.node_attr[Target]['HP'] <= 0:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                sys2.node_status[Target] = 'under_attack'
    return attack_orders

# 2
def low_ACK_attacking(sys1, sys2):
    attack_orders = {}
    ack_seq = sorted(sys1.G.nodes(), key=lambda i:sys1.node_attr[i]['ACK'], reverse=True)
    target_seq = sorted(sys2.G.nodes(), key=lambda i: sys2.node_attr[i]['ACK'], reverse=False)
    item = 0
    for attacker in ack_seq:
        if sys2.node_status[target_seq[item]] != 'destroyed':
            Target = target_seq[item]
            attack_orders[attacker] = {'team': [attacker], 'target': Target}
            sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            if sys2.node_attr[Target]['HP'] <= 0:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                sys2.node_status[Target] = 'under_attack'
        elif item+1 < sys2.N:
            item += 1
            Target = target_seq[item]
            attack_orders[attacker] = {'team': [attacker], 'target': Target}
            sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            if sys2.node_attr[Target]['HP'] <= 0:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                sys2.node_status[Target] = 'under_attack'
    return attack_orders

# 3
def high_DEF_attacking(sys1, sys2):
    attack_orders = {}
    ack_seq = sorted(sys1.G.nodes(), key=lambda i:sys1.node_attr[i]['ACK'], reverse=True)
    target_seq = sorted(sys2.G.nodes(), key=lambda i: sys2.node_attr[i]['DEF'], reverse=True)
    item = 0
    for attacker in ack_seq:
        if sys2.node_status[target_seq[item]] != 'destroyed':
            Target = target_seq[item]
            attack_orders[attacker] = {'team': [attacker], 'target': Target}
            sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            if sys2.node_attr[Target]['HP'] <= 0:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                sys2.node_status[Target] = 'under_attack'
        elif item+1 < sys2.N:
            item += 1
            Target = target_seq[item]
            attack_orders[attacker] = {'team': [attacker], 'target': Target}
            sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            if sys2.node_attr[Target]['HP'] <= 0:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                sys2.node_status[Target] = 'under_attack'
    return attack_orders

# 4
def high_ACK_attacking(sys1, sys2):
    attack_orders = {}
    ack_seq = sorted(sys1.G.nodes(), key=lambda i:sys1.node_attr[i]['ACK'], reverse=True)
    target_seq = sorted(sys2.G.nodes(), key=lambda i: sys2.node_attr[i]['ACK'], reverse=True)
    item = 0
    for attacker in ack_seq:
        if sys2.node_status[target_seq[item]] != 'destroyed':
            Target = target_seq[item]
            attack_orders[attacker] = {'team': [attacker], 'target': Target}
            sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            if sys2.node_attr[Target]['HP'] <= 0:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                sys2.node_status[Target] = 'under_attack'
        elif item+1 < sys2.N:
            item += 1
            Target = target_seq[item]
            attack_orders[attacker] = {'team': [attacker], 'target': Target}
            sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            if sys2.node_attr[Target]['HP'] <= 0:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                sys2.node_status[Target] = 'under_attack'
    return attack_orders

# 5
def low_DEF_low_ACK_attacking(sys1, sys2):
    attack_orders = {}
    ack_seq = sorted(sys1.G.nodes(), key=lambda i:sys1.node_attr[i]['ACK'], reverse=True)
    target_seq = sorted(sys2.G.nodes(), key=lambda i: sys2.node_attr[i]['ACK'] * sys2.node_attr[i]['DEF'],
                        reverse=False)
    item = 0
    for attacker in ack_seq:
        if sys2.node_status[target_seq[item]] != 'destroyed':
            Target = target_seq[item]
            attack_orders[attacker] = {'team': [attacker], 'target': Target}
            sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            if sys2.node_attr[Target]['HP'] <= 0:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                sys2.node_status[Target] = 'under_attack'
        elif item+1 < sys2.N:
            item += 1
            Target = target_seq[item]
            attack_orders[attacker] = {'team': [attacker], 'target': Target}
            sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            if sys2.node_attr[Target]['HP'] <= 0:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                sys2.node_status[Target] = 'under_attack'
    return attack_orders

# 6
def low_ACK_high_DEF_attacking(sys1, sys2):
    attack_orders = {}
    ack_seq = sorted(sys1.G.nodes(), key=lambda i:sys1.node_attr[i]['ACK'], reverse=True)
    target_seq = sorted(sys2.G.nodes(), key=lambda i: sys2.node_attr[i]['ACK'] / sys2.node_attr[i]['DEF'],
                        reverse=False)
    item = 0
    for attacker in ack_seq:
        if sys2.node_status[target_seq[item]] != 'destroyed':
            Target = target_seq[item]
            attack_orders[attacker] = {'team': [attacker], 'target': Target}
            sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            if sys2.node_attr[Target]['HP'] <= 0:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                sys2.node_status[Target] = 'under_attack'
        elif item+1 < sys2.N:
            item += 1
            Target = target_seq[item]
            attack_orders[attacker] = {'team': [attacker], 'target': Target}
            sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            if sys2.node_attr[Target]['HP'] <= 0:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                sys2.node_status[Target] = 'under_attack'
    return attack_orders

# 7
def high_ACK_low_DEF_attacking(sys1, sys2):
    attack_orders = {}
    ack_seq = sorted(sys1.G.nodes(), key=lambda i:sys1.node_attr[i]['ACK'], reverse=True)
    target_seq = sorted(sys2.G.nodes(), key=lambda i: sys2.node_attr[i]['ACK'] / sys2.node_attr[i]['DEF'],
                        reverse=True)
    item = 0
    for attacker in ack_seq:
        if sys2.node_status[target_seq[item]] != 'destroyed':
            Target = target_seq[item]
            attack_orders[attacker] = {'team': [attacker], 'target': Target}
            sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            if sys2.node_attr[Target]['HP'] <= 0:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                sys2.node_status[Target] = 'under_attack'
        elif item+1 < sys2.N:
            item += 1
            Target = target_seq[item]
            attack_orders[attacker] = {'team': [attacker], 'target': Target}
            sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            if sys2.node_attr[Target]['HP'] <= 0:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                sys2.node_status[Target] = 'under_attack'
    return attack_orders

# 8
def high_ACK_high_DEF_attacking(sys1, sys2):
    attack_orders = {}
    ack_seq = sorted(sys1.G.nodes(), key=lambda i:sys1.node_attr[i]['ACK'], reverse=True)
    target_seq = sorted(sys2.G.nodes(), key=lambda i: sys2.node_attr[i]['ACK'] * sys2.node_attr[i]['DEF'],
                        reverse=True)
    item = 0
    for attacker in ack_seq:
        if sys2.node_status[target_seq[item]] != 'destroyed':
            Target = target_seq[item]
            attack_orders[attacker] = {'team': [attacker], 'target': Target}
            sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            if sys2.node_attr[Target]['HP'] <= 0:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                sys2.node_status[Target] = 'under_attack'
        elif item+1 < sys2.N:
            item += 1
            Target = target_seq[item]
            attack_orders[attacker] = {'team': [attacker], 'target': Target}
            sys2.node_attr[Target]['HP'] -= sys1.node_attr[attacker]['ACK'] - sys2.node_attr[Target]['DEF']
            if sys2.node_attr[Target]['HP'] <= 0:
                sys2.node_attr[Target]['HP'] = 0
                sys2.node_status[Target] = 'destroyed'
            else:
                sys2.node_status[Target] = 'under_attack'
    return attack_orders
