# Your code should work with python 3.6 or less. Function/Method from python 3.8 are prohibited !!!
import math  # https://docs.python.org/3/library/math.html
from itertools import permutations

def calcul_distance(first_point_value, second_point_value):
    return math.sqrt(pow(second_point_value[0] - first_point_value[0], 2) + pow(second_point_value[1] - first_point_value[1], 2))


def calcul_circuit(list_of_points, cycle):
    length = 0
    for i in range(len(cycle) - 1):
        length += calcul_distance(list_of_points[cycle[i]], list_of_points[cycle[i + 1]])
    length += calcul_distance(list_of_points[cycle[len(cycle) - 1]], list_of_points[cycle[0]])
    return length


def nearest_neighbor_algorithm(first_point, list_of_points):
    cycle = {}
    list_of_left_points = list_of_points.copy()
    cycle[first_point] = list_of_left_points[first_point]
    del list_of_left_points[first_point]
    last_point = first_point
    while list_of_left_points:
        i = 0
        for key in list_of_left_points:
            if i == 0 :
                closest = key
                i += 1
            elif calcul_distance(cycle[last_point], list_of_left_points[key]) < calcul_distance(cycle[last_point], list_of_left_points[closest]):        
                closest = key
                i += 1
        cycle[closest] = list_of_left_points[closest]
        del list_of_left_points[closest]
        last_point = closest
    
    return list(cycle.keys())


def great_algorithm(first_point, list_of_points):
    
    t = tsp.tsp(list_of_points)
    print(t)
    
    
    



    return list(list_of_points.keys())


def optimal_algorithm(first_point, list_of_points):
    
    list_of_points_copy = list_of_points.copy()
    del list_of_points_copy[first_point]
    
    all_cycles = list(permutations(list_of_points_copy.keys(), len(list_of_points_copy)))
    all_cycles = [list(ele) for ele in all_cycles]
    
    optimalCycle = all_cycles.pop(0)
    optimalCycle.insert(0, first_point)
    
    for cycle in all_cycles:
        cycle.insert(0, first_point)
        if calcul_circuit(list_of_points, cycle) < calcul_circuit(list_of_points, optimalCycle) :
            optimalCycle = cycle
            
    return list(optimalCycle)


def get_small_list_of_points():
    list_of_points = {
        0: (1, 3),
        1: (2, 5),
        2: (0, 6),
        3: (1, 7),
        4: (5, 1),
        5: (5, 5),
        6: (6, 3),
        7: (4, 4),
        8: (7, 0),
        9: (6, 6)
    }
    return list_of_points


def test_calcul_distance():
    a = (-3, -2)
    b = (5, 2)
    assert round(calcul_distance(a, b), 3) == 8.944


def test_calcul_min_circuit():
    a = (-3, -2)
    b = (5, 2)
    list_of_points = {'a': a, 'b': b}
    cycle = ['a', 'b']

    assert round(calcul_circuit(list_of_points, cycle), 3) == 17.889


def test_calcul_circuit():
    list_of_points = get_small_list_of_points()
    cycle = list(list_of_points.keys())
    distance = calcul_circuit(list_of_points, cycle)
    
    assert round(distance, 3) == 38.483


def test_return_sized():
    list_of_points = get_small_list_of_points()

    first_point = 0
    result = nearest_neighbor_algorithm(first_point, list_of_points)
    assert len(result) == 10
    assert result[0] == first_point


def test_small_nearest_neighbor():
    list_of_points = get_small_list_of_points()
    first_point = 0
    result = nearest_neighbor_algorithm(first_point, list_of_points)
    assert len(result) == 10
    assert result[0] == first_point
    print(result)
    assert round(calcul_circuit(list_of_points, result)) <= 27


def test_big_nearest_neighbor():
    """I will test with a lot of points"""
    pass


def test_small_better_algorithm():
    list_of_points = get_small_list_of_points()

    first_point = 0
    result = great_algorithm(first_point, list_of_points)
    assert len(result) == 10
    assert result[0] == first_point

    """I will add some tests here"""


def test_big_better_algorithm():
    """I will test with a lot of points"""
    pass


def test_small_optimal_algorithm():
    list_of_points = get_small_list_of_points()

    first_point = 0
    result = optimal_algorithm(first_point, list_of_points)
    assert len(result) == 10
    assert result[0] == first_point

    """I will add some tests here"""


def test_big_optimal_algorithm():
    """I will test with a lot of points"""
    pass

test_small_better_algorithm()