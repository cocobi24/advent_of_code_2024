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

A.sort()
B.sort()
distance = 0
for i in range(len(A)):
    distance += abs(A[i] - B[i])
print(distance)