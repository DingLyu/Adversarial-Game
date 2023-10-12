# Codes and Platform for 

Paper: A Two-network Adversarial Game: Model, Strategy, and Structure

Platform: https://adversarialgame.dinglyu.cn/

Contact: Ding Lyu, dylan_lyu@sjtu.edu.cn or dylanlyu1225@gmail.com


## Code

### Dependencies
    Python, random, networkx, numpy, fa2, moviepy, seaborn, matplotlib


#### netsys.py: 
    class NetworkedSystem 
    def adversarial_systems_ws  # generate two adversarial WS small-world networks
    def adversarial_systems_powerlaw  # generate two adversarial networks with a power-law degree distribution 
    def adversarial_systems_ws_powerlaw  # generate a WS small-world network and a network with a power-law degree distribution
    

#### withoutcoop_confrontation_strategy.py: 
    ''' including without-coop confrontation strategies '''
    def low_DEF_attacking
    def low_ACK_attacking
    def high_DEF_attacking
    def high_ACK_attacking
    def low_DEF_low_ACK_attacking
    def low_ACK_high_DEF_attacking
    def high_ACK_low_DEF_attacking
    def high_ACK_high_DEF_attacking


#### cooperative_confrontation_strategy.py:
    ''' including cooperative confrontation strategies '''
    def cooperative_attacking
    def cooperative_attacking_degree
    def cooperative_attacking_clustering
    def cooperative_attacking_betweenness
    def cooperative_attacking_closeness

### simulations.py
    ''' compute the win rate in different cases '''
    def Net1_versus_Net2
    def winning_rate  # compute the win rate between different without-coop confrontation strategies
    def winning_rate_powerlaw # compute the win rate between the networks (employ ccs) with different power-law degree distributions
    def winning_rate_powerlaw_degree  # compute the win rate between the networks (employ ccs-k) with different power-law degree distributions
    def winning_rate_powerlaw_betweennes # compute the win rate between the networks (employ ccs-bet) with different power-law degree distributions
    def winning_rate_powerlaw_closeness  # compute the win rate between the networks (employ ccs-clo) with different power-law degree distributions
    def winning_rate_powerlaw_clustering  # compute the win rate between the networks (employ ccs-clu) with different power-law degree distributions
    def winning_rate_ws  # compute the win rate between two different WS small-world networks (employ ccs) 
    def winning_rate_ws_degree  # compute the win rate between two different WS small-world networks (employ ccs-k) 
    def winning_rate_ws_betweennes  # compute the win rate between two different WS small-world networks (employ ccs-bet) 
    def winning_rate_ws_closeness  # compute the win rate between two different WS small-world networks (employ ccs-clo) 
    def winning_rate_ws_clustering   # compute the win rate between two different WS small-world networks (employ ccs-clu) 

### visualization.py
    def trajectory # illustrate the dynamics of the two networks in a confrontation game
    def attacking_orders  # visualize the cooperative or adversarial relations in a confrontation game between a WS small-world network and a BA scale-free network
    def target_selection  # illustrate the target selection procedure of the four extended cooperative confrontation strategies
    def gif  # show a gif demo of a confrontation game between a WS small-world network and a BA scale-free network 

### utils.py
    const palette  # color selection for network visualization
    class forceatlas2  # calculate the layout of networks

### strategies.py
    ''' essentially the same as the cooperative_confrontation_strategy.py and withoutcoop_confrontation_strategy.py '''






