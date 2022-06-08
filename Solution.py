def Minimum_Operations (s):
    count = 0
    dict = {}
    for characters in s:
        if characters in dict:
            dict[characters] += 1
        else:
            dict[characters] = 1
    for i in dict:
        while dict[i] > 1:
            dict[i] -= 2
            count += 1
    return count

for _ in range(int(input())):
    n = int(input())
    s = input()

    out_ = Minimum_Operations(s)
    print (out_)
