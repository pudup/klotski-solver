# Klotski Solver

A simple Klotski puzzle solver written naively. Works from any position.

Uses BFS to find the shortest path. Takes about 18-22 seconds (deepcopy overhead?)


# Recursive Bruteforce Alternative

Uses bruteforce recursive backtracking, so it does not find the shortest path.

Takes 14025 moves to solve_recursive in 3-5 seconds. Just for fun :>
<br>
Maybe this can be improved?

# Pygame Animation

An animation in pygame-ce for the shortest path solution
<br>
Takes 18-22 seconds to spin up while it calculates the shortest path