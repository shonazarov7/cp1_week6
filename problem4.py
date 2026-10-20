def jump_limits(distances):
    #return (min(distances), max(distances))
    # shortest=min(distances)
    # longest=max(distances)
    # return (shortest, longest)
    shortest=distances[0]
    longest=distances[0]
    for d in distances:
        if d<shortest:
            shortest=d
        if d>longest:
            longest=d
    return (shortest, longest)
