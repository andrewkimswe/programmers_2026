from collections import deque

def get_node_count(start_node, skip_wire, adj, n):
    visited = [False] * (n + 1)
    visited[start_node] = True
    queue = deque([start_node])
    count = 1
    
    while queue:
        curr = queue.popleft()
        for neighbor in adj[curr]:
            if (curr == skip_wire[0] and neighbor == skip_wire[1]) or \
               (curr == skip_wire[1] and neighbor == skip_wire[0]):
                continue
            
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count

def solution(n, wires):
    adj = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        adj[v1].append(v2)
        adj[v2].append(v1)
    
    min_diff = n
    
    for wire in wires:
        count1 = get_node_count(wire[0], wire, adj, n)
        count2 = n - count1
        
        diff = abs(count1 - count2)
        
        min_diff = min(min_diff, diff)
        
    return min_diff