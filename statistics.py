import matplotlib.pyplot as plt

from netsys import *
from utils import *
from strategies import *

def statistics_winning_rate(epoches=10, runs=1000):
    confrontation_strategies = ['low_ACK_high_DEF_attacking', 'low_ACK_attacking',
                                'high_DEF_attacking', 'high_ACK_high_DEF_attacking',
                                'low_DEF_low_ACK_attacking', 'low_DEF_attacking',
                                'high_ACK_attacking', 'high_ACK_low_DEF_attacking'
                                ]
    ticks = ['low_$ack$\nhigh_$def$', 'low_$ack$', 'high_$def$', 'high_$ack$\nhigh_$def$',
             'low_$def$\nlow_$ack$', 'low_$def$', 'high_$ack$', 'high_$ack$\nlow_$def$']
    shape = (len(confrontation_strategies), len(confrontation_strategies))
    M = [[] for epoch in range(epoches)]
    for epoch in range(epoches):
        WR = []
        file = 'results/N100/withoutcoop/{}.txt'.format(epoch)
        with open(file, 'r') as f:
            for line in f.readlines():
                WR.append(line.strip('\n').split(','))
        M[epoch] = np.zeros(shape=shape)
        for wr in WR:
            if wr[2] == 'win':
                M[epoch][confrontation_strategies.index(wr[0]), confrontation_strategies.index(wr[1])] += 1.0 / runs
            if wr[2] == 'tie':
                M[epoch][confrontation_strategies.index(wr[0]), confrontation_strategies.index(wr[1])] += 0.5 / runs
    Mmean = np.mean(M, axis=0)
    for i in range(shape[0]):
        for j in range(shape[1]):
            Mmean[i][j] = int(Mmean[i][j] * 100)/100
    plt.figure(figsize=(10, 10))
    sns.heatmap(Mmean, cmap="YlGnBu", annot=True, xticklabels=ticks, yticklabels=ticks)
    plt.xticks(rotation=30, fontsize=15)
    plt.yticks(rotation=30, fontsize=15)
    plt.xlabel("$\pi_2$", fontsize=30)
    plt.ylabel("$\pi_1$", fontsize=30)
    plt.title("$N=100$", fontsize=30)
    plt.subplots_adjust(left=0.16, right=1, top=0.95, bottom=0.15)
    plt.savefig("figs/withoutcoop100.pdf")



def statistics_winning_rate_WS(epoches=10, runs=1000):
    P = ['0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9']
    shape = (len(P), len(P))
    M = [[] for epoch in range(epoches)]
    for epoch in range(epoches):
        WR = []
        file = 'results/N100/ccs/ws{}.txt'.format(epoch)
        with open(file, 'r') as f:
            for line in f.readlines():
                WR.append(line.strip('\n').split(','))
        M[epoch] = np.zeros(shape=shape)
        for wr in WR:
            if wr[2] == 'win':
                M[epoch][P.index(wr[0]), P.index(wr[1])] += 1.0 / runs
            if wr[2] == 'tie':
                M[epoch][P.index(wr[0]), P.index(wr[1])] += 0.5 / runs
    Mmean = np.mean(M, axis=0)
    for i in range(shape[0]):
        for j in range(shape[1]):
            Mmean[i][j] = int(Mmean[i][j] * 100)/100
    plt.figure(figsize=(7, 7))
    sns.heatmap(Mmean, cmap="YlGnBu", annot=True, xticklabels=P, yticklabels=P)
    plt.xticks(rotation=30, fontsize=20)
    plt.yticks(rotation=30, fontsize=20)
    plt.xlabel("$p_2$", fontsize=30)
    plt.ylabel("$p_1$", fontsize=30)
    plt.title("$N$=100, $<k>$=10, $\pi$=ccs", fontsize=30)
    plt.subplots_adjust(left=0.15, right=1, top=0.93, bottom=0.15)
    plt.savefig("figs/n100wsccs.pdf")


def statistics_winning_rate_WS_importance(epoches=10, runs=1000):
    P = ['0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9']
    shape = (len(P), len(P))
    M = [[] for epoch in range(epoches)]
    for epoch in range(epoches):
        WR = []
        file = 'results/N100/betweenness/ws{}.txt'.format(epoch)
        with open(file, 'r') as f:
            for line in f.readlines():
                WR.append(line.strip('\n').split(','))
        M[epoch] = np.zeros(shape=shape)
        for wr in WR:
            if wr[2] == 'win':
                M[epoch][P.index(wr[0]), P.index(wr[1])] += 1.0 / runs
            if wr[2] == 'tie':
                M[epoch][P.index(wr[0]), P.index(wr[1])] += 0.5 / runs
    Mmean = np.mean(M, axis=0)
    for i in range(shape[0]):
        for j in range(shape[1]):
            Mmean[i][j] = int(Mmean[i][j] * 100)/100
    plt.figure(figsize=(7, 7))
    sns.heatmap(Mmean, cmap="YlGnBu", annot=True, xticklabels=P, yticklabels=P)
    plt.xticks(rotation=30, fontsize=20)
    plt.yticks(rotation=30, fontsize=20)
    plt.xlabel("$p_2$", fontsize=30)
    plt.ylabel("$p_1$", fontsize=30)
    plt.title("$N$=100, $<k>$=10, $\pi$=ccs-$bet$", fontsize=30)
    plt.subplots_adjust(left=0.15, right=1, top=0.93, bottom=0.15)
    plt.savefig("figs/n100wsccsbet.pdf")



def statistics_winning_rate_heterogeneity(epoches=10, runs=1000):
    R = ['2.1', '2.5', '3', '5', '10']
    shape = (len(R), len(R))
    M = [[] for epoch in range(epoches)]
    for epoch in range(epoches):
        WR = []
        file = 'results/N100/ccs/hetero{}.txt'.format(epoch)
        with open(file, 'r') as f:
            for line in f.readlines():
                WR.append(line.strip('\n').split(','))
        M[epoch] = np.zeros(shape=shape)
        for wr in WR:
            if wr[2] == 'win':
                M[epoch][R.index(wr[0]), R.index(wr[1])] += 1.0 / runs
            if wr[2] == 'tie':
                M[epoch][R.index(wr[0]), R.index(wr[1])] += 0.5 / runs
    Mmean = np.mean(M, axis=0)
    for i in range(shape[0]):
        for j in range(shape[1]):
            Mmean[i][j] = int(Mmean[i][j] * 100)/100
    fig = plt.figure(figsize=(7, 7))
    sns.heatmap(Mmean, cmap="YlGnBu", annot=True, xticklabels=R, yticklabels=R)
    plt.xticks(rotation=30, fontsize=20)
    plt.yticks(rotation=30, fontsize=20)
    plt.xlabel("$\gamma_2$", fontsize=30)
    plt.ylabel("$\gamma_1$", fontsize=30)
    plt.title("$N$=100, $<k>$=10, $\pi$=ccs", fontsize=30)
    plt.subplots_adjust(left=0.15, right=1, top=0.93, bottom=0.15)
    plt.savefig('figs/n100baccs.pdf')



def statistics_winning_rate_heterogeneity_importance(epoches=10, runs=1000):
    R = ['2.1', '2.5', '3', '5', '10']
    shape = (len(R), len(R))
    M = [[] for epoch in range(epoches)]
    for epoch in range(epoches):
        WR = []
        file = 'results/N100/betweenness/hetero{}.txt'.format(epoch)
        with open(file, 'r') as f:
            for line in f.readlines():
                WR.append(line.strip('\n').split(','))
        M[epoch] = np.zeros(shape=shape)
        for wr in WR:
            if wr[2] == 'win':
                M[epoch][R.index(wr[0]), R.index(wr[1])] += 1.0 / runs
            if wr[2] == 'tie':
                M[epoch][R.index(wr[0]), R.index(wr[1])] += 0.5 / runs
    Mmean = np.mean(M, axis=0)
    for i in range(shape[0]):
        for j in range(shape[1]):
            Mmean[i][j] = int(Mmean[i][j] * 100)/100
    fig = plt.figure(figsize=(7, 7))
    sns.heatmap(Mmean, cmap="YlGnBu", annot=True, xticklabels=R, yticklabels=R)
    plt.xticks(rotation=30, fontsize=20)
    plt.yticks(rotation=30, fontsize=20)
    plt.xlabel("$\gamma_2$", fontsize=30)
    plt.ylabel("$\gamma_1$", fontsize=30)
    plt.title("$N$=100, $<k>$=10, $\pi$=ccs-$bet$", fontsize=30)
    plt.subplots_adjust(left=0.15, right=1, top=0.93, bottom=0.15)
    plt.savefig('figs/n100baccsbet.pdf')




def statistics_winning_rate_heterogeneity1(epoches=10, runs=1000):
    R = ['2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '3.0']
    shape = (len(R), len(R))
    M = [[] for epoch in range(epoches)]
    for epoch in range(epoches):
        WR = []
        file = 'results/N100/ccs/23hetero{}.txt'.format(epoch)
        with open(file, 'r') as f:
            for line in f.readlines():
                WR.append(line.strip('\n').split(','))
        M[epoch] = np.zeros(shape=shape)
        for wr in WR:
            if wr[2] == 'win':
                M[epoch][R.index(wr[0]), R.index(wr[1])] += 1.0 / runs
            if wr[2] == 'tie':
                M[epoch][R.index(wr[0]), R.index(wr[1])] += 0.5 / runs
    Mmean = np.mean(M, axis=0)
    for i in range(shape[0]):
        for j in range(shape[1]):
            Mmean[i][j] = int(Mmean[i][j] * 100)/100
    fig = plt.figure(figsize=(7, 7))
    sns.heatmap(Mmean, cmap="YlGnBu", annot=True, xticklabels=R, yticklabels=R)
    plt.xticks(rotation=30, fontsize=20)
    plt.yticks(rotation=30, fontsize=20)
    plt.xlabel("$\gamma_2$", fontsize=30)
    plt.ylabel("$\gamma_1$", fontsize=30)
    plt.title("$N$=100, $<k>$=10, $\pi$=ccs", fontsize=30)
    plt.subplots_adjust(left=0.15, right=1, top=0.93, bottom=0.15)
    plt.savefig('figs/n100ba2ccs.pdf')



def statistics_winning_rate_heterogeneity_importance1(epoches=10, runs=1000):
    R = ['2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '3.0']
    shape = (len(R), len(R))
    M = [[] for epoch in range(epoches)]
    for epoch in range(epoches):
        WR = []
        file = 'results/N100/degree/23hetero{}.txt'.format(epoch)
        with open(file, 'r') as f:
            for line in f.readlines():
                WR.append(line.strip('\n').split(','))
        M[epoch] = np.zeros(shape=shape)
        for wr in WR:
            if wr[2] == 'win':
                M[epoch][R.index(wr[0]), R.index(wr[1])] += 1.0 / runs
            if wr[2] == 'tie':
                M[epoch][R.index(wr[0]), R.index(wr[1])] += 0.5 / runs
    Mmean = np.mean(M, axis=0)
    for i in range(shape[0]):
        for j in range(shape[1]):
            Mmean[i][j] = int(Mmean[i][j] * 100)/100
    fig = plt.figure(figsize=(7, 7))
    sns.heatmap(Mmean, cmap="YlGnBu", annot=True, xticklabels=R, yticklabels=R)
    plt.xticks(rotation=30, fontsize=20)
    plt.yticks(rotation=30, fontsize=20)
    plt.xlabel("$\gamma_2$", fontsize=30)
    plt.ylabel("$\gamma_1$", fontsize=30)
    plt.title("$N$=100, $<k>$=10, $\pi$=ccs-$k$", fontsize=30)
    plt.subplots_adjust(left=0.15, right=1, top=0.93, bottom=0.15)
    plt.savefig('figs/n100ba2ccsk.pdf')
