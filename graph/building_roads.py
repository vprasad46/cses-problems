
















if __name__== "__main__":
    n, m = input().split(" ")
    n, m = int(n), int(m)
    parent_map = dict()
    parent = set([str(i+1) for i in range(n)])

    for i in range(m):
        _from, _to = input().split(" ")
        
        if _from not in parent_map and _to not in parent_map:
            parent_map[_from] = _from
            parent_map[_to] = _from
            parent.remove(_to)
        elif _from not in parent_map and _to in parent_map:
            og_parent = parent[_to]
            while parent_map[og_parent] == og_parent:
                og_parent = parent_map[og_parent]
            parent_map[_from] = og_parent
        elif _from in parent_map and _to not in parent_map:
            og_parent = parent_map[_from]
            while parent_map[og_parent] == og_parent:
                og_parent = parent_map[og_parent]
            parent_map[_to] = og_parent
