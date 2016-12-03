#!/usr/bin/env python
#coding: utf-8
import networkx as nx
import matplotlib.pyplot as plt

t_start = 0
t_end = 1000000000

def static_paths(G, x, v):
    path_list = []
    for path in nx.all_simple_paths(G, x, v):
        if path not in path_list:
            path_list.append(path)
        else:
            continue
    return path_list


def edges_of_path(G, path):
    """
    example:
    input: G is temporal graph path = ['a', 'c', 'h', 'i', 'l']
    output: [('a', 'c', {0: {'duraTime': 1, 'startTime': 4}}),
            ('c', 'h', {0: {'duraTime': 1, 'startTime': 6}}),
            ('h', 'i', {0: {'duraTime': 1, 'startTime': 7}})，
            ('i', 'l', {0: {'duraTime': 1, 'startTime': 9}, 1: {'duraTime': 1, 'startTime': 8}})]
    """
    index = len(path) -1
    convert_path = range(index+1)
    if index == 0:
        convert_path[index] = path[index]       
    while index > 0:
        convert_path[index-1] = (path[index-1], path[index],G.get_edge_data(path[index-1], path[index]))                 
        index -= 1  
    return convert_path


def quad_triple(e):
    """
    input : e = ('a', 'c', {0: {'duraTime': 1, 'startTime': 4}}
    output:　a list [('a', 'c', 4, 1)] 
    """
    if len(e[2]) == 1:
        return [(e[0], e[1], e[2][0]['startTime'], e[2][0]['duraTime'])]
    
    if len(e[2]) > 1:
        i = len(e[2]) - 1
        e_list = []
        while i >= 0:
            e_list.append((e[0], e[1], e[2][i]['startTime'], e[2][i]['duraTime']))

        return e_list
    else:
        return None




def quad_tuple_paths(convert_path):
    """
    input: [('a', 'c', {0: {'duraTime': 1, 'startTime': 4}}),
            ('c', 'h', {0: {'duraTime': 1, 'startTime': 6}}),
            ('h', 'i', {0: {'duraTime': 1, 'startTime': 7}})，
            ('i', 'l', {0: {'duraTime': 1, 'startTime': 9}, 1: {'duraTime': 1, 'startTime': 8}})]

    output: paths = [path1, path2] path1 = [e1, e2, e3, e4] e1 = ('a', 'c', 4, 1), e2=('c', 'h', 6, 1)..,e4=('i', 'l', 8, 1)
                                   path2 = [e1, e2, e3, e4'] e1 = ('a', 'c', 4, 1), e2=('c', 'h', 6, 1)..,e4=('i', 'l', 9, 1)
    """
    path = []
    for e in convert_path:
        et_list = quad_tuple(e)
        path.extend(et_list)

    return path





def is_temp_path(path):
    """
    input path = [e1, e2,...], e1 = ('a', 'b', 3, 1)
    output True or False
    """
    if len(path) <= 1:
        return True

    for i in range(len(path)-1):
         if (path[i][2] + path[i][3]) <= path[i+1][2]:
             continue
         else:
             return False
    return True





if __name__ == "__main__":
    t_alpha = 0
    t_beta = 10

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
