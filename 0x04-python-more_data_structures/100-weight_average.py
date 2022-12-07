#!/usr/bin/python3
def weight_average(my_list=[]):
    total_weight = 0
    total_score = 0
    for score, weight in my_list:
        total_score += (score * weight)
        total_weight += weight
    return total_score / total_weight
