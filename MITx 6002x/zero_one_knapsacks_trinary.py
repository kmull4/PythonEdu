items = ['a', 'b', 'c']

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1: # ">>" = i // 2**j
                combo.append(items[j])
        yield combo

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i // 3**j) % 3 == 1: # ">>" = i // 2**j
                bag1.append(items[j])
            elif (i // 3**j) % 3 == 2: # ">>" = i // 2**j
                bag2.append(items[j])
        yield (bag1, bag2)
