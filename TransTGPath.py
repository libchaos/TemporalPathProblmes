#!/usr/bin/env python
#coding: utf-8
import networkx as nx
import matplotlib.pyplot as plt

def quad_tuple(edge):
    result = []
    edge_data = TG.get_edge_data(*(edge))
    len_edge_data = len(edge_data)
    if len_edge_data == 1:
        result.append(edge + (edge_data[0]['startTime'], edge_data[0]['duraTime']))
    if len_edge_data > 1:
        for i in range(len_edge_data):
            result.append(edge + (edge_data[i]['startTime'], edge_data[i]['duraTime']))

    return result


if __name__ == "__main__":


    TG = nx.MultiDiGraph()

   

    TG.add_edge('a', 'b', startTime=1, duraTime=1)
    TG.add_edge('a', 'b', startTime=2, duraTime=1)
    TG.add_edge('a', 'c', startTime=2, duraTime=1)
    TG.add_edge('a', 'c', startTime=4, duraTime=1)
    TG.add_edge('b', 'f', startTime=5, duraTime=1)
    TG.add_edge('c', 'f', startTime=6, duraTime=1)
    TG.add_edge('c', 'g', startTime=7, duraTime=1)
    

    quad_tuple_edges = []
    memo = []
    for edge in nx.edges_iter(TG):
        if edge not in memo:
            memo.append(edge)
            r = quad_tuple(edge)
            quad_tuple_edges.extend(r)
        else:
            continue

    edge_stream = sorted(quad_tuple_edges, key = lambda item: item[2])

    TDG = nx.DiGraph()

    # add edge where duraTime = 1 
    for e in edge_stream:
        TDG.add_edge((e[0], e[2]), (e[1], e[2]+e[3]), duraTime=1)
    
    #add edge where duraTime = 0

    nodes = sorted(TDG.nodes(), key=lambda item: (item[0], item[1]))

    len_nodes = len(nodes)
    for i in range(len_nodes-1):
        if nodes[i][0] == nodes[i+1][0]:
            TDG.add_edge(nodes[i], nodes[i+1], duraTime=0)
    

    

    nx.shortest_path(TDG, ('a', 4), ('g', 8))


    