from netsys import *
from utils import *
from withoutcoop_confrontation_strategy import *
from cooperative_confrontation_strategy import *
from multiprocessing import Process

def Net1_versus_Net2(opt1, opt2):
    sys1, sys2 = adversarial_systems_ws(N=100, num_neighbors=4, p1=0.1, p2=0.1)
    while sys1.G.nodes() and sys2.G.nodes():
        if opt1 == 'low_DEF_attacking':
            attack_orders1 = low_DEF_attacking(sys1, sys2)
        if opt1 == 'low_ACK_attacking':
            attack_orders1 = low_ACK_attacking(sys1, sys2)
        if opt1 == 'high_DEF_attacking':
            attack_orders1 = high_DEF_attacking(sys1, sys2)
        if opt1 == 'high_ACK_attacking':
            attack_orders1 = high_ACK_attacking(sys1, sys2)
        if opt1 == 'low_DEF_low_ACK_attacking':
            attack_orders1 = low_DEF_low_ACK_attacking(sys1, sys2)
        if opt1 == 'low_ACK_high_DEF_attacking':
            attack_orders1 = low_ACK_high_DEF_attacking(sys1, sys2)
        if opt1 == 'high_ACK_low_DEF_attacking':
            attack_orders1 = high_ACK_low_DEF_attacking(sys1, sys2)
        if opt1 == 'high_ACK_high_DEF_attacking':
            attack_orders1 = high_ACK_high_DEF_attacking(sys1, sys2)
        if opt2 == 'low_DEF_attacking':
            attack_orders2 = low_DEF_attacking(sys2, sys1)
        if opt2 == 'low_ACK_attacking':
            attack_orders2 = low_ACK_attacking(sys2, sys1)
        if opt2 == 'high_DEF_attacking':
            attack_orders2 = high_DEF_attacking(sys2, sys1)
        if opt2 == 'high_ACK_attacking':
            attack_orders2 = high_ACK_attacking(sys2, sys1)
        if opt2 == 'low_DEF_low_ACK_attacking':
            attack_orders2 = low_DEF_low_ACK_attacking(sys2, sys1)
        if opt2 == 'low_ACK_high_DEF_attacking':
            attack_orders2 = low_ACK_high_DEF_attacking(sys2, sys1)
        if opt2 == 'high_ACK_low_DEF_attacking':
            attack_orders2 = high_ACK_low_DEF_attacking(sys2, sys1)
        if opt2 == 'high_ACK_high_DEF_attacking':
            attack_orders2 = high_ACK_high_DEF_attacking(sys2, sys1)
        sys1._update_system()
        sys2._update_system()
        if not sys1.G.nodes() and not sys2.G.nodes():
            return 'tie'
        elif not sys1.G.nodes():
            return 'loss'
        elif not sys2.G.nodes():
            return 'win'


def winning_rate(epoch, runs=1000):
    T0 = time.time()
    WR = []
    confrontation_strategies = ['low_DEF_attacking', 'low_ACK_attacking', 'high_DEF_attacking', 'high_ACK_attacking',
                                'low_DEF_low_ACK_attacking', 'low_ACK_high_DEF_attacking', 'high_ACK_low_DEF_attacking',
                                'high_ACK_high_DEF_attacking']
    for i in range(len(confrontation_strategies)):
        for j in range(len(confrontation_strategies)):
            for _ in range(runs):
                WR.append([confrontation_strategies[i], confrontation_strategies[j], Net1_versus_Net2(confrontation_strategies[i], confrontation_strategies[j])])
    file = 'results/N100/withoutcoop/{}.txt'.format(epoch)
    with open(file, 'w') as f:
        for wr in WR:
            f.write(','.join(wr) + '\n')
    print(epoch, time.time()-T0, file)

def Net1_versus_Net2_powerlaw(gamma1, gamma2):
    sys1, sys2 = adversarial_systems_powerlaw(N=100, M=5, gamma1=gamma1, gamma2=gamma2)
    while sys1.G.nodes() and sys2.G.nodes():
        attack_orders1 = cooperative_attacking(sys1, sys2)
        attack_orders2 = cooperative_attacking(sys2, sys1)
        sys1._update_system()
        sys2._update_system()
        if not sys1.G.nodes() and not sys2.G.nodes():
            return 'tie'
        elif not sys1.G.nodes():
            return 'loss'
        elif not sys2.G.nodes():
            return 'win'

def Net1_versus_Net2_powerlaw_degree(gamma1, gamma2):
    sys1, sys2 = adversarial_systems_powerlaw(N=100, M=5, gamma1=gamma1, gamma2=gamma2)
    while sys1.G.nodes() and sys2.G.nodes():
        attack_orders1 = cooperative_attacking_degree(sys1, sys2)
        attack_orders2 = cooperative_attacking_degree(sys2, sys1)
        sys1._update_system()
        sys2._update_system()
        if not sys1.G.nodes() and not sys2.G.nodes():
            return 'tie'
        elif not sys1.G.nodes():
            return 'loss'
        elif not sys2.G.nodes():
            return 'win'

def Net1_versus_Net2_powerlaw_betweenness(gamma1, gamma2):
    sys1, sys2 = adversarial_systems_powerlaw(N=100, M=5, gamma1=gamma1, gamma2=gamma2)
    while sys1.G.nodes() and sys2.G.nodes():
        attack_orders1 = cooperative_attacking_betweenness(sys1, sys2)
        attack_orders2 = cooperative_attacking_betweenness(sys2, sys1)
        sys1._update_system()
        sys2._update_system()
        if not sys1.G.nodes() and not sys2.G.nodes():
            return 'tie'
        elif not sys1.G.nodes():
            return 'loss'
        elif not sys2.G.nodes():
            return 'win'

def Net1_versus_Net2_powerlaw_clustering(gamma1, gamma2):
    sys1, sys2 = adversarial_systems_powerlaw(N=100, M=5, gamma1=gamma1, gamma2=gamma2)
    while sys1.G.nodes() and sys2.G.nodes():
        attack_orders1 = cooperative_attacking_clustering(sys1, sys2)
        attack_orders2 = cooperative_attacking_clustering(sys2, sys1)
        sys1._update_system()
        sys2._update_system()
        if not sys1.G.nodes() and not sys2.G.nodes():
            return 'tie'
        elif not sys1.G.nodes():
            return 'loss'
        elif not sys2.G.nodes():
            return 'win'

def Net1_versus_Net2_powerlaw_closeness(gamma1, gamma2):
    sys1, sys2 = adversarial_systems_powerlaw(N=100, M=5, gamma1=gamma1, gamma2=gamma2)
    while sys1.G.nodes() and sys2.G.nodes():
        attack_orders1 = cooperative_attacking_closeness(sys1, sys2)
        attack_orders2 = cooperative_attacking_closeness(sys2, sys1)
        sys1._update_system()
        sys2._update_system()
        if not sys1.G.nodes() and not sys2.G.nodes():
            return 'tie'
        elif not sys1.G.nodes():
            return 'loss'
        elif not sys2.G.nodes():
            return 'win'

def winning_rate_powerlaw(epoch, runs=1000):
    T0 = time.time()
    WR = []
    gamma = [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0]
    for i in range(len(gamma)):
        for j in range(len(gamma)):
            for _ in range(runs):
                WR.append([str(gamma[i]), str(gamma[j]), Net1_versus_Net2_powerlaw(gamma[i], gamma[j])])
    file = 'results/N100/ccs/23hetero{}.txt'.format(epoch)
    with open(file, 'w') as f:
        for wr in WR:
            f.write(','.join(wr) + '\n')
    print(epoch, time.time()-T0, file)

def winning_rate_powerlaw_degree(epoch, runs=1000):
    T0 = time.time()
    WR = []
    gamma = [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0]
    for i in range(len(gamma)):
        for j in range(len(gamma)):
            for _ in range(runs):
                WR.append([str(gamma[i]), str(gamma[j]), Net1_versus_Net2_powerlaw_degree(gamma[i], gamma[j])])
    file = 'results/N100/degree/23hetero{}.txt'.format(epoch)
    with open(file, 'w') as f:
        for wr in WR:
            f.write(','.join(wr) + '\n')
    print(epoch, time.time()-T0, file)

def winning_rate_powerlaw_betweenness(epoch, runs=1000):
    T0 = time.time()
    WR = []
    gamma = [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0]
    for i in range(len(gamma)):
        for j in range(len(gamma)):
            for _ in range(runs):
                WR.append([str(gamma[i]), str(gamma[j]), Net1_versus_Net2_powerlaw_betweenness(gamma[i], gamma[j])])
    file = 'results/N100/betweenness/23hetero{}.txt'.format(epoch)
    with open(file, 'w') as f:
        for wr in WR:
            f.write(','.join(wr) + '\n')
    print(epoch, time.time()-T0, file)

def winning_rate_powerlaw_closeness(epoch, runs=1000):
    T0 = time.time()
    WR = []
    gamma = [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0]
    for i in range(len(gamma)):
        for j in range(len(gamma)):
            for _ in range(runs):
                WR.append([str(gamma[i]), str(gamma[j]), Net1_versus_Net2_powerlaw_closeness(gamma[i], gamma[j])])
    file = 'results/N100/closeness/23hetero{}.txt'.format(epoch)
    with open(file, 'w') as f:
        for wr in WR:
            f.write(','.join(wr) + '\n')
    print(epoch, time.time()-T0, file)

def winning_rate_powerlaw_clustering(epoch, runs=1000):
    T0 = time.time()
    WR = []
    gamma = [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0]
    for i in range(len(gamma)):
        for j in range(len(gamma)):
            for _ in range(runs):
                WR.append([str(gamma[i]), str(gamma[j]), Net1_versus_Net2_powerlaw_clustering(gamma[i], gamma[j])])
    file = 'results/N100/clustering/23hetero{}.txt'.format(epoch)
    with open(file, 'w') as f:
        for wr in WR:
            f.write(','.join(wr) + '\n')
    print(epoch, time.time()-T0, file)

def winning_rate_powerlaw1(epoch, runs=1000):
    T0 = time.time()
    WR = []
    gamma = [2.1, 2.5, 3, 5, 10]
    for i in range(len(gamma)):
        for j in range(len(gamma)):
            for _ in range(runs):
                WR.append([str(gamma[i]), str(gamma[j]), Net1_versus_Net2_powerlaw(gamma[i], gamma[j])])
    file = 'results/N100/ccs/hetero{}.txt'.format(epoch)
    with open(file, 'w') as f:
        for wr in WR:
            f.write(','.join(wr) + '\n')
    print(epoch, time.time()-T0, file)

def winning_rate_powerlaw_degree1(epoch, runs=1000):
    T0 = time.time()
    WR = []
    gamma = [2.1, 2.5, 3, 5, 10]
    for i in range(len(gamma)):
        for j in range(len(gamma)):
            for _ in range(runs):
                WR.append([str(gamma[i]), str(gamma[j]), Net1_versus_Net2_powerlaw_degree(gamma[i], gamma[j])])
    file = 'results/N100/degree/hetero{}.txt'.format(epoch)
    with open(file, 'w') as f:
        for wr in WR:
            f.write(','.join(wr) + '\n')
    print(epoch, time.time()-T0, file)

def winning_rate_powerlaw_betweenness1(epoch, runs=1000):
    T0 = time.time()
    WR = []
    gamma = [2.1, 2.5, 3, 5, 10]
    for i in range(len(gamma)):
        for j in range(len(gamma)):
            for _ in range(runs):
                WR.append([str(gamma[i]), str(gamma[j]), Net1_versus_Net2_powerlaw_betweenness(gamma[i], gamma[j])])
    file = 'results/N100/betweenness/hetero{}.txt'.format(epoch)
    with open(file, 'w') as f:
        for wr in WR:
            f.write(','.join(wr) + '\n')
    print(epoch, time.time()-T0, file)

def winning_rate_powerlaw_closeness1(epoch, runs=1000):
    T0 = time.time()
    WR = []
    gamma = [2.1, 2.5, 3, 5, 10]
    for i in range(len(gamma)):
        for j in range(len(gamma)):
            for _ in range(runs):
                WR.append([str(gamma[i]), str(gamma[j]), Net1_versus_Net2_powerlaw_closeness(gamma[i], gamma[j])])
    file = 'results/N100/closeness/hetero{}.txt'.format(epoch)
    with open(file, 'w') as f:
        for wr in WR:
            f.write(','.join(wr) + '\n')
    print(epoch, time.time()-T0, file)

def winning_rate_powerlaw_clustering1(epoch, runs=1000):
    T0 = time.time()
    WR = []
    gamma = [2.1, 2.5, 3, 5, 10]
    for i in range(len(gamma)):
        for j in range(len(gamma)):
            for _ in range(runs):
                WR.append([str(gamma[i]), str(gamma[j]), Net1_versus_Net2_powerlaw_clustering(gamma[i], gamma[j])])
    file = 'results/N100/clustering/hetero{}.txt'.format(epoch)
    with open(file, 'w') as f:
        for wr in WR:
            f.write(','.join(wr) + '\n')
    print(epoch, time.time()-T0, file)

def Net1_versus_Net2_ws(p1, p2):
    sys1, sys2 = adversarial_systems_ws(N=100, num_neighbors=10, p1=p1, p2=p2)
    while sys1.G.nodes() and sys2.G.nodes():
        attack_orders1 = cooperative_attacking(sys1, sys2)
        attack_orders2 = cooperative_attacking(sys2, sys1)
        sys1._update_system()
        sys2._update_system()
        if not sys1.G.nodes() and not sys2.G.nodes():
            return 'tie'
        elif not sys1.G.nodes():
            return 'loss'
        elif not sys2.G.nodes():
            return 'win'

def Net1_versus_Net2_ws_degree(p1, p2):
    sys1, sys2 = adversarial_systems_ws(N=100, num_neighbors=10, p1=p1, p2=p2)
    while sys1.G.nodes() and sys2.G.nodes():
        attack_orders1 = cooperative_attacking_degree(sys1, sys2)
        attack_orders2 = cooperative_attacking_degree(sys2, sys1)
        sys1._update_system()
        sys2._update_system()
        if not sys1.G.nodes() and not sys2.G.nodes():
            return 'tie'
        elif not sys1.G.nodes():
            return 'loss'
        elif not sys2.G.nodes():
            return 'win'

def Net1_versus_Net2_ws_betweenness(p1, p2):
    sys1, sys2 = adversarial_systems_ws(N=100, num_neighbors=10, p1=p1, p2=p2)
    while sys1.G.nodes() and sys2.G.nodes():
        attack_orders1 = cooperative_attacking_betweenness(sys1, sys2)
        attack_orders2 = cooperative_attacking_betweenness(sys2, sys1)
        sys1._update_system()
        sys2._update_system()
        if not sys1.G.nodes() and not sys2.G.nodes():
            return 'tie'
        elif not sys1.G.nodes():
            return 'loss'
        elif not sys2.G.nodes():
            return 'win'

def Net1_versus_Net2_ws_closeness(p1, p2):
    sys1, sys2 = adversarial_systems_ws(N=100, num_neighbors=10, p1=p1, p2=p2)
    while sys1.G.nodes() and sys2.G.nodes():
        attack_orders1 = cooperative_attacking_closeness(sys1, sys2)
        attack_orders2 = cooperative_attacking_closeness(sys2, sys1)
        sys1._update_system()
        sys2._update_system()
        if not sys1.G.nodes() and not sys2.G.nodes():
            return 'tie'
        elif not sys1.G.nodes():
            return 'loss'
        elif not sys2.G.nodes():
            return 'win'

def Net1_versus_Net2_ws_clustering(p1, p2):
    sys1, sys2 = adversarial_systems_ws(N=100, num_neighbors=10, p1=p1, p2=p2)
    while sys1.G.nodes() and sys2.G.nodes():
        attack_orders1 = cooperative_attacking_clustering(sys1, sys2)
        attack_orders2 = cooperative_attacking_clustering(sys2, sys1)
        sys1._update_system()
        sys2._update_system()
        if not sys1.G.nodes() and not sys2.G.nodes():
            return 'tie'
        elif not sys1.G.nodes():
            return 'loss'
        elif not sys2.G.nodes():
            return 'win'

def winning_rate_ws(epoch, runs=1000):
    T0 = time.time()
    WR = []
    P = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    for i in range(len(P)):
        for j in range(len(P)):
            for _ in range(runs):
                WR.append([str(P[i]), str(P[j]), Net1_versus_Net2_ws(P[i], P[j])])
    file = 'results/N100/ccs/ws{}.txt'.format(epoch)
    with open(file, 'w') as f:
        for wr in WR:
            f.write(','.join(wr) + '\n')
    print(epoch, time.time()-T0, file)

def winning_rate_ws_degree(epoch, runs=1000):
    T0 = time.time()
    WR = []
    P = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    for i in range(len(P)):
        for j in range(len(P)):
            for _ in range(runs):
                WR.append([str(P[i]), str(P[j]), Net1_versus_Net2_ws_degree(P[i], P[j])])
    file = 'results/N100/degree/ws{}.txt'.format(epoch)
    with open(file, 'w') as f:
        for wr in WR:
            f.write(','.join(wr) + '\n')
    print(epoch, time.time()-T0, file)

def winning_rate_ws_betweenness(epoch, runs=1000):
    T0 = time.time()
    WR = []
    P = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    for i in range(len(P)):
        for j in range(len(P)):
            for _ in range(runs):
                WR.append([str(P[i]), str(P[j]), Net1_versus_Net2_ws_betweenness(P[i], P[j])])
    file = 'results/N100/betweenness/ws{}.txt'.format(epoch)
    with open(file, 'w') as f:
        for wr in WR:
            f.write(','.join(wr) + '\n')
    print(epoch, time.time()-T0, file)

def winning_rate_ws_closeness(epoch, runs=1000):
    T0 = time.time()
    WR = []
    P = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    for i in range(len(P)):
        for j in range(len(P)):
            for _ in range(runs):
                WR.append([str(P[i]), str(P[j]), Net1_versus_Net2_ws_closeness(P[i], P[j])])
    file = 'results/N100/closeness/ws{}.txt'.format(epoch)
    with open(file, 'w') as f:
        for wr in WR:
            f.write(','.join(wr) + '\n')
    print(epoch, time.time()-T0, file)

def winning_rate_ws_clustering(epoch, runs=1000):
    T0 = time.time()
    WR = []
    P = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    for i in range(len(P)):
        for j in range(len(P)):
            for _ in range(runs):
                WR.append([str(P[i]), str(P[j]), Net1_versus_Net2_ws_clustering(P[i], P[j])])
    file = 'results/N100/clustering/ws{}.txt'.format(epoch)
    with open(file, 'w') as f:
        for wr in WR:
            f.write(','.join(wr) + '\n')
    print(epoch, time.time()-T0, file)



if __name__ == '__main__':
    process_list = []
    for i in range(10):
        p = Process(target=winning_rate, args=(i,))
        p.start()
        process_list.append(p)
    for i in range(10):
        p = Process(target=winning_rate_powerlaw, args=(i,))
        p.start()
        process_list.append(p)
    for i in range(10):
        p = Process(target=winning_rate_powerlaw_degree, args=(i,))
        p.start()
        process_list.append(p)
    for i in range(10):
        p = Process(target=winning_rate_powerlaw_betweenness, args=(i,))
        p.start()
        process_list.append(p)
    for i in range(10):
        p = Process(target=winning_rate_powerlaw_closeness, args=(i,))
        p.start()
        process_list.append(p)
    for i in range(10):
        p = Process(target=winning_rate_powerlaw_clustering, args=(i,))
        p.start()
        process_list.append(p)
    for i in range(10):
        p = Process(target=winning_rate_powerlaw1, args=(i,))
        p.start()
        process_list.append(p)
    for i in range(10):
        p = Process(target=winning_rate_powerlaw_degree1, args=(i,))
        p.start()
        process_list.append(p)
    for i in range(10):
        p = Process(target=winning_rate_powerlaw_betweenness1, args=(i,))
        p.start()
        process_list.append(p)
    for i in range(10):
        p = Process(target=winning_rate_powerlaw_closeness1, args=(i,))
        p.start()
        process_list.append(p)
    for i in range(10):
        p = Process(target=winning_rate_powerlaw_clustering1, args=(i,))
        p.start()
        process_list.append(p)
    for i in range(10):
        p = Process(target=winning_rate_ws, args=(i,))
        p.start()
        process_list.append(p)
    for i in range(10):
        p = Process(target=winning_rate_ws_degree, args=(i,))
        p.start()
        process_list.append(p)
    for i in range(10):
        p = Process(target=winning_rate_ws_betweenness, args=(i,))
        p.start()
        process_list.append(p)
    for i in range(10):
        p = Process(target=winning_rate_ws_closeness, args=(i,))
        p.start()
        process_list.append(p)
    for i in range(10):
        p = Process(target=winning_rate_ws_clustering, args=(i,))
        p.start()
        process_list.append(p)
    for i in process_list:
        p.join()

