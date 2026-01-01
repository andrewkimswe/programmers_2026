def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
def union_parent(parent, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    
    parent = [i for i in range(n)]
    edges = 0
    
    for start, end, cost in costs:
        if find_parent(parent, start) != find_parent(parent, end):
            union_parent(parent, start, end)
            answer += cost
            edges += 1
            
            if edges == n - 1:
                break
    
    return answer