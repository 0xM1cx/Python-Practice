def SecondMaxOfThreeNumbers():
    N = input().split(" ")
    N = [int(x) for x in N]


    for i in N:
        if i > max(N) and i < min(N):
            print(i)


SecondMaxOfThreeNumbers()