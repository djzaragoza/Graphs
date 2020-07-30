
def earliest_ancestor(ancestors, starting_node):
    # dictionary of ancestors -- family
    family = {}

    # loop -- if the elder is not in the faily dict set it to the first position, otherwise, append it to the dict
    for elder in ancestors:
        if elder[1] not in family:
            family[elder[1]] = [elder[0]]
        else:
            family[elder[1]].append(elder[0])

    # if starting node has no family then just exit
    if starting_node not in family:
        return - 1
        
    # set current_gen equal to the parent dict at the starting node so we can
    current_gen = family[starting_node]

    while True:
        # doing a loop through the elders in the current generation to add them to the new gen and comparing it to current gen (which set to equal to starting node of family dict)
        new_gen = []
        for elder in current_gen:
            if elder in family:
                new_gen = new_gen + family[elder]

            if len(new_gen) == 0:
                return current_gen[0]
            else:
                current_gen = new_gen
    pass