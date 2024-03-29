###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # Helper function. Returns a tuple with optimal cow's name and weight, or
    # returns None if no valid cows.
    def largest_can_fit(cows_copy, remaining_limit):
        weight = -1
        for c in cows_copy:
            if cows_copy[c] > weight and cows_copy[c] <= remaining_limit:
                name = c
                weight = cows_copy[c]
        if weight == -1: # no valid cows
            return None
        else:
            return (name, weight)
    
    # initialize a few things
    cows_copy = cows.copy()
    master_list = []
    this_trip = []
    remaining_limit = limit
    while len(cows_copy) > 0:
        # go through the cows and find highest at or below the limit
        best_cow = largest_can_fit(cows_copy, remaining_limit)
        if best_cow == None: # no more valid cows
            master_list.append(this_trip)
            this_trip = []
            remaining_limit = limit
            continue
        # from here we assume we have a valid cow
        this_trip.append(str(best_cow[0]))
        # subtract from weight limit
        remaining_limit -= best_cow[1]
        # and remove the cow from cows_copy
        del cows_copy[str(best_cow[0])]
    # add the last trip that didn't make it through the while loop
    master_list.append(this_trip)
    return master_list


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # it worked last time and helped me keep organized
    cows_copy = cows.copy()
    lowest_edge = len(cows_copy) # track the answer with lowest possible edges
    
    # since get_partitions takes in a list and not a dictionary, make list
    cow_list = []
    for i in cows.copy():
        cow_list.append(i) # add the keys
    
    # call get_partitions() with the list of cows
    for combo in (get_partitions(cow_list)):
        # see if combo is valid
        weight_broken = 0 # how many trips in combo break the weight limit
        num_trips = 0
        for trip in combo: # determine if trip breaks weight limit
            num_trips += 1    
            total = 0
            for item in trip:
                total += cows_copy[item] # adding in each cow
            if total > limit: # limit broken
                    weight_broken += 1
        if weight_broken > 0:
            continue # moves to the next combo of trips
        else: # combo is valid
            # find number of edges (trips). if lower, make this the new answer
            if num_trips <= lowest_edge:
                lowest_edge = num_trips
                answer = combo
    return answer


# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # greedy algo
    start = time.time()
    num_trips = len(greedy_cow_transport(cows,limit))
    end = time.time()
    print('greedy =', num_trips, 'trips,', end - start, 'seconds')
    
    # brute force algo
    start = time.time()
    num_trips = len(brute_force_cow_transport(cows,limit))
    end = time.time()
    print('brute =', num_trips, 'trips,', end - start, 'seconds')
    return


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows,'\n')

#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))
compare_cow_transport_algorithms()