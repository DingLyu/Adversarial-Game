import networkx as nx

from utils import *

class NetworkedSystem(object):
    def __init__(self, name):
        super(NetworkedSystem, self).__init__()
        self.system_name = name
        self.N = 0
        self.E = 0
        self.G = nx.DiGraph()
        self.node_status = {}
        self.node_attr = {}
        self.coop_cost = {}

    def _random_system_ws(self, num_nodes, num_neighbors, attr, p):
        if p != 0:
            self.G = nx.random_graphs.watts_strogatz_graph(n=num_nodes, k=num_neighbors, p=p).to_directed()
        else:
            self.G = nx.random_graphs.random_regular_graph(d=num_neighbors, n=num_nodes).to_directed()
        self.N = nx.number_of_nodes(self.G)
        self.E = nx.number_of_edges(self.G)
        self.node_status = {i: 'active' for i in np.arange(self.N)}

        df = pd.DataFrame(attr, columns=['ACK', 'DEF', 'HP', 'LS'])
        for index, row in df.iterrows():
            self.node_attr[index] = row

        for edge in self.G.edges():
            self.coop_cost[edge] = 1
        for node in self.G.nodes():
            self.coop_cost[(node, node)] = 0

    def _random_system_powerlaw(self, num_nodes, M, attr, gamma):
        self.G = self.G_price_model(N=num_nodes, M=M, gamma=gamma)
        self.N = nx.number_of_nodes(self.G)
        self.E = nx.number_of_edges(self.G)
        self.node_status = {i: 'active' for i in np.arange(self.N)}

        df = pd.DataFrame(attr, columns=['ACK', 'DEF', 'HP', 'LS'])
        for index, row in df.iterrows():
            self.node_attr[index] = row

        for edge in self.G.edges():
            self.coop_cost[edge] = 1
        for node in self.G.nodes():
            self.coop_cost[(node, node)] = 0

    def _update_system(self):
        Nodes = list(self.G.nodes()).copy()
        for node in Nodes:
            if self.node_status[node] == 'destroyed':
                self.G.remove_node(node)
        self.N = nx.number_of_nodes(self.G)
        self.E = nx.number_of_edges(self.G)

    def G_price_model(self, N, M, gamma):
        p = 1 / (gamma - 1)
        G = nx.Graph()
        G1 = nx.DiGraph()
        m0 = M
        Array = ['1', '1', '2', '1', '3']
        G.add_edges_from([('2', '1'), ('3', '1'), ('4', '1'), ('4', '3'), ('3', '2')])
        G1.add_edges_from([(1, 0), (0, 1), (2, 0), (0, 2), (3, 0), (0, 3),
                           (3, 2), (2, 3), (2, 1), (1, 2)])
        m = M
        for i in range(m0 + 1, N + 1):
            temp = []
            while len(temp) < m:
                r = random.random()
                if r < p:
                    t = random.choice(Array)
                else:
                    t = str(random.randint(1, i - 1))
                if t in temp:
                    continue
                else:
                    temp.append(t)
            for j in temp:
                G.add_edge(str(i), str(j))
                G1.add_edge(int(i) - 1, int(j) - 1)
                G1.add_edge(int(j) - 1, int(i) - 1)
            Array.extend(temp)
        return G1


def adversarial_systems_ws(N=20, num_neighbors=8, p1=0.3, p2=0.3):
    SYSTEM_RED_NAME = 'I'
    SYSTEM_BLUE_NAME = 'II'
    sys1 = NetworkedSystem(name=SYSTEM_RED_NAME)
    sys2 = NetworkedSystem(name=SYSTEM_BLUE_NAME)
    Attack = np.random.randint(11, 21, (N, 1))
    Defense = np.random.randint(1, 11, (N, 1))
    Health = np.random.randint(80, 121, (N, 1))
    Leadership = 0.5 * np.random.random((N, 1)) + 1
    Attr = np.concatenate((Attack, Defense, Health, Leadership), axis=1)
    Attr1 = Attr.copy()
    Attr2 = Attr.copy()
    sys1._random_system_ws(num_nodes=N, num_neighbors=num_neighbors, attr=Attr1, p=p1)
    sys2._random_system_ws(num_nodes=N, num_neighbors=num_neighbors, attr=Attr2, p=p2)
    return sys1, sys2


def adversarial_systems_powerlaw(N=20, M=5, gamma1=3, gamma2=3):
    SYSTEM_RED_NAME = 'I'
    SYSTEM_BLUE_NAME = 'II'
    sys1 = NetworkedSystem(name=SYSTEM_RED_NAME)
    sys2 = NetworkedSystem(name=SYSTEM_BLUE_NAME)
    Attack = np.random.randint(11, 21, (N, 1))
    Defense = np.random.randint(1, 11, (N, 1))
    Health = np.random.randint(80, 121, (N, 1))
    Leadership = 0.5 * np.random.random((N, 1)) + 1
    Attr = np.concatenate((Attack, Defense, Health, Leadership), axis=1)
    Attr1 = Attr.copy()
    Attr2 = Attr.copy()
    sys1._random_system_powerlaw(num_nodes=N, M=M, attr=Attr1, gamma=gamma1)
    sys2._random_system_powerlaw(num_nodes=N, M=M, attr=Attr2, gamma=gamma2)
    return sys1, sys2


def adversarial_systems_ws_powerlaw(N=20, M=5, num_neighbors=8, p1=0.3, gamma2=3):
    SYSTEM_RED_NAME = 'I'
    SYSTEM_BLUE_NAME = 'II'
    sys1 = NetworkedSystem(name=SYSTEM_RED_NAME)
    sys2 = NetworkedSystem(name=SYSTEM_BLUE_NAME)
    Attack = np.random.randint(11, 21, (N, 1))
    Defense = np.random.randint(1, 11, (N, 1))
    Health = np.random.randint(80, 121, (N, 1))
    Leadership = 0.5 * np.random.random((N, 1)) + 1
    Attr = np.concatenate((Attack, Defense, Health, Leadership), axis=1)
    Attr1 = Attr.copy()
    Attr2 = Attr.copy()
    sys1._random_system_ws(N, num_neighbors=num_neighbors, attr=Attr1, p=p1)
    sys2._random_system_powerlaw(num_nodes=N, M=M, attr=Attr2, gamma=gamma2)
    return sys1, sys2



