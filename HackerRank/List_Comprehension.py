from itertools import permutations

i = int(input())
j = int(input())
k = int(input())
n = 3


arr = [[a,b,c] for a in [i,j,k] for b in [i,j,k] for c in [i,j,k]]


print([[d,f,g] for d,f,g in arr if (d+f+g) != n])