from collections import deque
import heapq

class WaterNetwork:
    def __init__(self, junction_count):
        self.connections = {i: [] for i in range(junction_count)}

    def connect(self, source, target, weight):
        self.connections[source].append((target, weight))
        self.connections[target].append((source, weight))


def breadth_first_search(net, source, target):
    to_visit = deque([(source, [source])])
    explored = set()

    while to_visit:
        node, route = to_visit.popleft()

        if node == target:
            return route

        if node not in explored:
            explored.add(node)
            for neighbor, _ in net.connections[node]:
                if neighbor not in explored:
                    to_visit.append((neighbor, route + [neighbor]))

    return None


def depth_first_search(net, node, target, seen=None, trail=None):
    if seen is None:
        seen = set()
    if trail is None:
        trail = []

    seen.add(node)
    trail.append(node)

    if node == target:
        return trail

    for neighbor, _ in net.connections[node]:
        if neighbor not in seen:
            result = depth_first_search(net, neighbor, target, seen, trail)
            if result:
                return result

    trail.pop()
    return None


def limited_depth_search(net, node, target, depth, seen=None, trace=None):
    if seen is None:
        seen = set()
    if trace is None:
        trace = []

    seen.add(node)
    trace.append(node)

    if node == target:
        return trace
    if depth == 0:
        seen.remove(node)
        trace.pop()
        return None

    for neighbor, _ in net.connections[node]:
        if neighbor not in seen:
            outcome = limited_depth_search(net, neighbor, target, depth - 1, seen, trace)
            if outcome:
                return outcome

    seen.remove(node)
    trace.pop()
    return None


def iterative_deep_search(net, start, target, max_depth):
    for d in range(max_depth + 1):
        outcome = limited_depth_search(net, start, target, d)
        if outcome:
            return outcome
    return None


def cost_based_search(net, start, target):
    priority_queue = [(0, start, [start])]
    min_cost_map = {}

    while priority_queue:
        curr_cost, node, route = heapq.heappop(priority_queue)

        if node == target:
            return route, curr_cost

        if node in min_cost_map and min_cost_map[node] <= curr_cost:
            continue

        min_cost_map[node] = curr_cost

        for neighbor, weight in net.connections[node]:
            heapq.heappush(priority_queue, (curr_cost + weight, neighbor, route + [neighbor]))

    return None, float("inf")


def run_interface():
    junctions, pipes = map(int, input("Enter total junctions and total connections: ").split())
    system = WaterNetwork(junctions)

    print("Now provide each connection as: <from> <to> <flow cost>")
    for _ in range(pipes):
        a, b, cost = map(int, input().split())
        system.connect(a, b, cost)

    source = int(input("\nStart junction: "))
    destination = int(input("Target junction: "))

    print("\n>> ROUTING RESULTS <<")
    print("BFS (no cost considered):", breadth_first_search(system, source, destination))
    print("DFS (no cost considered):", depth_first_search(system, source, destination))

    limit = int(input("\nSet depth for limited DFS: "))
    print("Depth-Limited Search:", limited_depth_search(system, source, destination, limit))

    max_d = int(input("\nSet max depth for iterative search: "))
    print("Iterative Deepening:", iterative_deep_search(system, source, destination, max_d))

    result_path, path_cost = cost_based_search(system, source, destination)
    print(f"\nUniform Cost Search: Path → {result_path} | Total Cost → {path_cost}")


if __name__ == "__main__":
    run_interface()
