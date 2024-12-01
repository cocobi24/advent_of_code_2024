# https://adventofcode.com/2024/day/1

import sys
input = sys.stdin

A, B = [], []
while True:
    line = input.readline().rstrip()
    if line == "":
        break
    a, b = map(int, line.split())
    A.append(a)
    B.append(b)

# Part 1
def get_Ansert_Part1():
    A.sort()
    B.sort()
    distance = 0
    l = len(A)
    for i in range(l):
        distance += abs(A[i] - B[i])
    print(distance)


# Part 2
def get_Ansert_Part2():
    similarity_set = {} # value=[cnt, qty]
    l = len(A)
    for i in range(l):
        if A[i] not in similarity_set:
            similarity_set[A[i]] = [0, 1]
        else:
            similarity_set[A[i]][1] += 1

    for i in range(l):
        if B[i] in similarity_set:
            similarity_set[B[i]][0] += 1

    similarity = 0
    for k, v in similarity_set.items():
        similarity += int(k) * v[0] * v[1]
    print(similarity)

get_Ansert_Part1()
get_Ansert_Part2()