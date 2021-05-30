import sys

Visited = {}
Dependencies = {}

# Total cost of the for-loop: O(n^2)
# For every input line, we iterate through all dependencies
for input in sys.stdin:

    input = input.strip().split()
    ll = len(input)

    if ll >= 1:

        p = input[0]

        if p not in Dependencies:
            Dependencies[p] = []

        for i in range(1, ll):
            pi = input[i]
            if pi not in Dependencies:
                Dependencies[pi] = []
            Dependencies[pi].append(p)

# Total cost of the for-loop: O(n^3)
for D in Dependencies: # Complexity at this time: O(n)

    Visited = {}

    queue = []
    queue_pointer = 0
    queue.append(D)

    counter = 0

    while queue_pointer < len(queue): # Complexity at this time: O(n^2)

        current = queue[queue_pointer]
        queue_pointer += 1

        for di in Dependencies[current]: # Complexity at this time: O(n^3)
            if di not in Visited:
                Visited[di] = "Visited"
                counter += 1
                queue.append(di)
    
    print(counter, D)


# Complexity analysis:
# Worst case: O(n^3) - Every software package depends on all other possible
# software packages. The graph is a completely connected graph.
# Best case: O(n) - No package depends on any other package. Every package
# is a separate connected component of the graph.



