parent=dict()
rank=dict()
def make_set(vertice):
    parent[vertice]=vertice
    rank[vertice]=0
def find(vertice):
    if parent[vertice]!=vertice:
        parent[vertice]=find(parent[vertice])
    return parent[vertice]
def union(v1,v2):
    r1=find(v1)
    r2=find(v2)
    if rank[r1]>rank[r2]:
        parent[r2]=r1
    elif rank[r1]<rank[r2]:
        parent[r1]=r2
    else:
        parent[r1]=r2
        rank[r2]+=1
def kruskal(graph):
    for v in graph['vertices']:
        make_set(v)
    mst=set()
    edges=list(graph['edges'])
    edges.sort()
    for edge in edges:
        w,v1,v2=edge
        if find(v1)!=find(v2):
            union(v1,v2)
            mst.add(edge)
    return sorted(mst)
graph = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
'edges': set([
(7, 'A', 'B'),
(5, 'A', 'D'),
(7, 'B', 'A'),
(8, 'B', 'C'),
(9, 'B', 'D'),
(7, 'B', 'E'),
(8, 'C', 'B'),
(5, 'C', 'E'),
(5, 'D', 'A'),
(9, 'D', 'B'),
(7, 'D', 'E'),
(6, 'D', 'F'),
(7, 'E', 'B'),
(5, 'E', 'C'),
(15, 'E', 'D'),
(8, 'E', 'F'),
(9, 'E', 'G'),
(6, 'F', 'D'),
(8, 'F', 'E'),
(11, 'F', 'G'),
(9, 'G', 'E'),
(11, 'G', 'F'),
])
}

print(kruskal(graph))
        
