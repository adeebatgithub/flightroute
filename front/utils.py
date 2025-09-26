import heapq

from front.models import AirportModel, RouteModel


def find_nth_node(start, direction, n):
    current_airport = AirportModel.objects.get(code=start)

    steps = 0
    while steps < n:
        try:
            route = RouteModel.objects.get(starting=current_airport, position=direction)
        except RouteModel.DoesNotExist:
            return None
        current_airport = route.ending
        steps += 1

    return current_airport


def find_longest_path_from_airport():
    start_airport = AirportModel.objects.first()

    def dfs(current_airport, duration=0, path=None):
        if path is None:
            path = [current_airport]

        # Get all outgoing routes
        routes = RouteModel.objects.filter(starting=current_airport)

        if not routes.exists():
            return path, duration

        longest_path = (path, duration)

        for route in routes:
            new_path, new_duration = dfs(
                route.ending,
                duration + route.duration,
                path + [route.ending]
            )
            if new_duration > longest_path[1]:
                longest_path = (new_path, new_duration)

        return longest_path

    final_path, total_duration = dfs(start_airport)

    return {
        "path": final_path,
        "duration": total_duration
    }


def find_shortest_path(start, end):
    starting = AirportModel.objects.get(code=start)
    ending = AirportModel.objects.get(code=end)

    pq = [(0, starting.id, starting, [starting])]
    visited = set()

    while pq:
        duration, _, current_airport, path = heapq.heappop(pq)

        if current_airport == ending:
            return {
                "path": path,
                "duration": duration
            }

        if current_airport in visited:
            continue

        visited.add(current_airport)

        for route in RouteModel.objects.filter(starting=current_airport):
            if route.ending not in visited:
                heapq.heappush(
                    pq,
                    (duration + route.duration, route.ending.id, route.ending, path + [route.ending])
                )

    return None
