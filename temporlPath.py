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


def earliest_arrival_time(TG, edge_stream, x, t_start, t_end):
    t = {}
    t[x] = t_start 
    for node in TG.nodes_iter():
        if node == x:
            continue
        t[node] = float('inf')
    for edge in edge_stream:
        if edge[2] + edge[3] <= t_end and edge[2] >= t[edge[0]]:
            if edge[2] + edge[3] < t[edge[1]]:
                t[edge[1]] = edge[2] + edge[3]
            elif edge[2] >= t_end:
                break
    return t


def latest_departure_time(TG, reversed_edge_stream, x, t_start, t_end):
    t = {}
    t[x] = t_end
    for node in TG.nodes_iter():
        if node == x:
            continue
        t[node] = -float('inf')
    for edge in reversed_edge_stream:
        if edge[2] >= t_start:
            if edge[2] + edge[3] <= t[edge[1]]:
                if edge[2] > t[edge[0]]:
                    t[edge[0]] = edge[2]
        else:
            break
    
    return t

    





if __name__ == "__main__":


    TG = nx.MultiDiGraph()

    TG.add_nodes_from(['a', 'b', 'c', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])

    TG.add_edge('a', 'b', startTime=1, duraTime=1)
    TG.add_edge('a', 'b', startTime=2, duraTime=1)
    TG.add_edge('a', 'c', startTime=4, duraTime=1)
    TG.add_edge('a', 'f', startTime=3, duraTime=1)
    TG.add_edge('a', 'i', startTime=10, duraTime=1)
    TG.add_edge('b', 'g', startTime=3, duraTime=1)
    TG.add_edge('b', 'h', startTime=3, duraTime=1)
    TG.add_edge('c', 'h', startTime=6, duraTime=1)
    TG.add_edge('f', 'i', startTime=5, duraTime=1)
    TG.add_edge('g', 'j', startTime=2, duraTime=1)
    TG.add_edge('g', 'k', startTime=6, duraTime=1)
    TG.add_edge('h', 'k', startTime=7, duraTime=1)
    TG.add_edge('h', 'i', startTime=7, duraTime=1)
    TG.add_edge('i', 'l', startTime=9, duraTime=1)
    TG.add_edge('i', 'l', startTime=8, duraTime=1)



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


    print earliest_arrival_time(TG, edge_stream, 'a', 1, 4)
    print latest_departure_time(TG, reversed(edge_stream), 'l', 1, 10)

    