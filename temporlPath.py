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

    
def mutli_pass_fatest_path_duration(TG, edge_stream, x, t_start, t_end):
  
    f = {}
    t = {}
    f[x] = 0
    S = set()
    for node in TG.nodes_iter():
        if node == x:
            continue
        f[node] = float('inf')
    for edge in edge_stream:
        if x == edge[0] and edge[2] >= t_start and (edge[2] + edge[3]) <= t_end:
            S.add(edge)

    
    for e in list(S):
        earliest_times = earliest_arrival_time(TG, edge_stream, e[1], t_start+e[3]+e[2], t_end)
        print earliest_times
        for key, value in earliest_times.items():
                if key != x and f[key] > 0:
                    f[key] = min(f[key], earliest_times[key] - e[2]) 
       
    return f
    

def create_L_v(TG, edge_stream, x, t_start, t_end):
    L = {}
    arrive_times = earliest_arrival_time(TG, edge_stream, x, t_start, t_end)
    for key, value in arrive_times.items():
        L[key] = (t_start, value)
    
    return sorted(L.items(), key=lambda item: item[1])

def one_pass_fatest_path_duration1(TG, edge_stream, x, t_start, t_end):
    
    L = {}   
    f = {}
    f[x] = 0
    for node in TG.nodes_iter():
        L[node] = []
        if node == x:
            continue
        f[node] = float('inf')
    
    for edge in edge_stream:
        u = edge[0]
        v = edge[1]
        t = edge[2]
        duraT = edge[3]
        if t >= t_start and t + duraT <= t_end:
            l = [u].extend([i[1] for i  in TG.out_edges(x)])
            for x in l:
                if u == x:
                    if (t, t) not in L[x]:
                        L[x].append((t, t))
                
                max_i = max(L[u], key=lambda item: item[1])
                a1_u = max_i[1]
                s1_u = max_i[0]
                s_v = s1_u
                a_v = t + duraT
                for item in L[v]:
                    if s_v == item[0]:
                        item[1] = a_v
                        break
                else:
                    L[v].append((s_v, a_v))
                L[v].pop(0)
                if a_v - s_v < f[v]:
                    f[v] = a_v - s_v
        else:
            break
    return f

            
             


    

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


    # print earliest_arrival_time(TG, edge_stream, 'a', 1, 4)
    # print latest_departure_time(TG, reversed(edge_stream), 'l', 1, 10)
    # print fatest_path_duration1(TG, edge_stream, 'a', 0, 10)

    # print create_L_v(TG, edge_stream, 'a', 0, 10)
    print one_pass_fatest_path_duration1(TG, edge_stream, 'a', 0, 10)