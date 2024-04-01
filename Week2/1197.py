# from queue import PriorityQueue

# v, e = map(int,input().split())

# connet_info = []
# node_list = []
# for i in range(1, v+1):
#     node_list.append(i)
#     connet_info.append(i)

# edge_info =[]
# for i in range(e):
#     a,b,c = map(int,input().split())
#     d = {'from':a,'to':b,'cost':c}
#     edge_info.append(d)
# print(edge_info)

# for i in node_list:
#     parrent_node = edge_info[i]

#     min_val = 1000000
#     for j in edge_info: # node i 에서 출발하는 간선들중 가중치가 가장 작은 간선을 찾는다
#         if j['from'] == i:
#             if min_val > j['cost'] : min_val = j['cost']
        

import sys
import heapq
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
V, E = map(int,sys.stdin.readline().split())
parent = [i for i in range(V+1)]
cost = []
sum = 0
cnt = 0
for _ in range(E):
    A, B, C = map(int,sys.stdin.readline().split())
    heapq.heappush(cost,(C, A, B))
# print(parent)
# print(cost)
while cnt < V-1 and cost:
    c, a, b = heapq.heappop(cost)
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a != b:
        union_parent(parent,a,b)
        cnt += 1
        sum += c
print(sum)