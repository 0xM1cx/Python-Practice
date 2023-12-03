import matplotlib
import numpy
import math
from scipy import stats

def populationVariance(n):
    mean = sum(n)/len(n)
    n_sum = 0
    for i in n:
        n_sum += (i - mean)**2
    
    return n_sum / len(n)
def sampleVariance(n):
    mean = sum(n)/len(n)
    n_sum = 0
    for i in n:
        n_sum += (i - mean)**2

    return n_sum / (len(n) - 1)

def getData(n):

    print(f"Mean: {sum(n)/len(n)}")
    if len(n) % 2 == 0:
        print(f"Median: {n[int(len(n)/2-1)] + n[int(len(n)/2) - 1]}")
    else:
        print(f"Median: {n[int((len(n)/2)-1) - 1]}")

    res = stats.mode(n)
    print(f"Mode: {res.mode, res.count}")
    print(f"Min: {min(n)}")
    print(f"Max: {max(n)}")
    print(f"Range: {max(n) - min(n)}")
    print(f"IQR: {numpy.percentile(n, 75) - numpy.percentile(n, 25)}") 
    print(f"Population Variance: {round(populationVariance(n), 4)}")
    print(f"Sample Variance: {round(sampleVariance(n), 4)}")
    print(f"Population Standard Deviation: {round(math.sqrt(populationVariance(n)), 4)}")
    print(f"Sample Standard Deviation: {round(math.sqrt(sampleVariance(n)), 4)}")
    print(f"Coefficient of Variation: {round((sampleVariance(n) / (sum(n)/len(n))) * 100, 4)}")
    print(f"76th percentile: {n[int((76 * (len(n) + 1)) / 100) - 1]}")
    print(f"85th percentile: {n[int((85 * (len(n) + 1)) / 100) - 1]}")
    print(f"6th decile: {n[int((6 * (len(n) + 1)) / 100) - 1]}")

    
def main():
    n = input("INPUT: ").split(" ")
    print(len(n))
    n = [int(i) for i in n] 
    print(sorted(n))
    getData(n)


main()
