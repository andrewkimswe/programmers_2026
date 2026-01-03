from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for s, e in tickets:
        graph[s].append(e)
    
    for s in graph:
        graph[s].sort(reverse=True)

    stack = ["ICN"]
    path = []

    while stack:
        curr = stack[-1]
        if curr in graph and graph[curr]:
            stack.append(graph[curr].pop())
        else:
            path.append(stack.pop())

    return path[::-1]