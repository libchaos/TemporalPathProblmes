#!/usr/bin/env python
#coding: utf-8
import networkx as nx
import matplotlib.pyplot as plt




if __name__ == "__main__":


    MG = nx.MultiDiGraph()

    MG.add_nodes_from(['a', 'b', 'c', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])

    MG.add_edge('a', 'b', startTime=1, duraTime=1)
    MG.add_edge('a', 'b', startTime=2, duraTime=1)
    MG.add_edge('a', 'c', startTime=4, duraTime=1)
    MG.add_edge('a', 'f', startTime=3, duraTime=1)
    MG.add_edge('a', 'i', startTime=10, duraTime=1)
    MG.add_edge('b', 'g', startTime=3, duraTime=1)
    MG.add_edge('b', 'h', startTime=3, duraTime=1)
    MG.add_edge('c', 'h', startTime=6, duraTime=1)
    MG.add_edge('f', 'i', startTime=5, duraTime=1)
    MG.add_edge('g', 'j', startTime=2, duraTime=1)
    MG.add_edge('g', 'k', startTime=6, duraTime=1)
    MG.add_edge('h', 'k', startTime=7, duraTime=1)
    MG.add_edge('h', 'i', startTime=7, duraTime=1)
    MG.add_edge('i', 'l', startTime=9, duraTime=1)
    MG.add_edge('i', 'l', startTime=8, duraTime=1)

    # nx.draw_networkx(MG, pos=nx.spring_layout(MG))
    # plt.show()

    # find_all_temp_path(MG, 'a', 'l')


    # path = edges_of_path(MG, ['a', 'c', 'h', 'i', 'l'])
    # is_temp_path(path)
