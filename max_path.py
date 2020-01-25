from collections import defaultdict


def solve(paths):
    paths_found = defaultdict(list)
    paths_length = defaultdict(int)
    max_path = 0
    for city in paths.keys():
        for next_city, distance in paths[city]:
            current_path = 0
            neighbors = paths.get(city)
            while neighbors:
                current_path += distance
                if current_path > max_path:
                    max_path = current_path
                neighbors = paths.get(next_city)
                paths_found[city].append(next_city)
                paths_length[city] += distance

    return max_path


cities = {"A": [("B", 2), ("C", 1)], "B": [("D", 3)], "C": [("E", 1), ("F", 2), ("G", 5)]}
assert 6 == solve(cities)
