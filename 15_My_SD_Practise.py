#
# Hansen
# 2024/11/6
# Standard Deviatiom

import statistics
import math


def my_sd(input):
    print(f'Input:{input}')
    length = len(input)
    sum = 0
    output = 0 
    mean =  statistics.mean(input)
    print(f'Mean: {mean}')
    for x in input:
        sum += (int(x) - mean ) ** 2 
    sum= sum / length
    output = math.sqrt(sum)
    return output

answer = my_sd([1,2,3])
answer = round(answer,5)
print(f'Answer:{answer}')