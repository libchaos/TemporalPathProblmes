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
    TG.add_edge('a', 'c', startTime=4, duraTime=1)
    TG.add_edge('c', 'a', startTime=6, duraTime=1)
    TG.add_edge('b', 'd', startTime=4, duraTime=1)
    TG.add_edge('c', 'd', startTime=5, duraTime=1)
   
    

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

    # # add edge where duraTime = 1 
    # for e in edge_stream:
    #     TDG.add_edge((e[0], e[2]), (e[1], e[2]+e[3]), duraTime=1)
    
    # #add edge where duraTime = 0

    # nodes = sorted(TDG.nodes(), key=lambda item: (item[0], item[1]))

    # len_nodes = len(nodes)
    # for i in range(len_nodes-1):
    #     if nodes[i][0] == nodes[i+1][0]:
    #         TDG.add_edge(nodes[i], nodes[i+1], duraTime=0)
    
    
    
    V_in = {}
    V_out = {}
    for e in edge_stream:
        V_out[e[0]] = []
        V_in[e[1]] = []
    for e in edge_stream:
        V_out[e[0]].append((e[0], e[2])) 
        V_in[e[1]].append((e[1], e[2]+e[3]))

    print V_in
    print V_out

    for key, value in V_in.items():

        l = len(value)
        if l == 1:
            TDG.add_node(value[0])
        if l > 1:          
            for i in range(l-1):
                TDG.add_edge(value[i], value[i+1])
        else:
            break

    for key, value in V_out.items():
        l = len(value)
        if l == 1:
            TDG.add_node(value[0])
        if l > 1:          
            for i in range(l-1):
                TDG.add_edge(value[i], value[i+1])
        else:
            break
    


    for in_key, in_value in V_in.items():
        for out_key, out_value in V_out.items():
            if in_key == out_key and max(in_value)[1] <= min(out_value)[1]:
                TDG.add_edge(max(in_value, key=lambda item: item[1]), min(out_value, key=lambda item: item[1]))


    for e in edge_stream:
        print e
        TDG.add_edge((e[0], e[2]), (e[1], e[2]+e[3]))

    print "test"
