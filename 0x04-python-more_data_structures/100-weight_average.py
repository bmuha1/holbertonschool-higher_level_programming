#!/usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    weight = 0
    for i in range(len(my_list)):
        my_list[i] += (0, 0)
        score += my_list[i][0] * my_list[i][1]
        weight += my_list[i][1]
    if weight == 0:
        return 0
    else:
        return score / weight
