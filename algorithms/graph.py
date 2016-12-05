# reference:
# https://www.python.org/doc/essays/graphs/

def find_path(graph, start, end, path=[]):
    if start not in graph:
        return None

    path = path + [start]
    if end == start:
        return path

    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


def find_all_paths(graph, start, end, path=[]):
    if start not in graph:
        return []

    path = path + [start] # it's not equal to path += [start]
    if end == start:
        return [path]

    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_shortest_path(graph, start, end, path=[]):
    if start not in graph:
        return None

    path = path + [start] # it's not equal to path += [start]
    if end == start:
        return path

    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(shortest) > len(newpath):
                    shortest = newpath
    return shortest


def main():
    # a direct graph
    graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

    # print find_path(graph, 'A', 'D')
    # print find_all_paths(graph, 'A', 'D')
    print find_shortest_path(graph, 'A', 'D')


if __name__ == '__main__':
    main()