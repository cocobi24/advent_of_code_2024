import sys
input = sys.stdin

lines = []
while True:
  row = list(map(int, input.readline().rstrip().split()))
  if not row:
    break
  lines.append(row)

def Q1_SOLUTION(line):
  sline = sorted(line)
  l = len(line)
  if line == sline or line == sline[::-1]:
    for i in range(1, l):
      if abs(line[i] - line[i - 1]) > 3 or line[i] == line[i - 1]:
        return False
    return True
  return False


def Q2_SOLUTION(line):
  sline = sorted(line)
  l = len(line)
  if line == sline or line == sline[::-1]:
    for i in range(1, l):
      if abs(line[i] - line[i - 1]) > 3 or line[i] == line[i - 1]:
        a = line[:i] + line[i + 1 :]
        b = line[: i - 1] + line[i:]
        return Q1_SOLUTION(a) or Q1_SOLUTION(b)
    return True
  else:
    for i in range(0, l):
      a = line[:i] + line[i + 1 :]
      if Q1_SOLUTION(a):
        return True
  return False

Q1_ANSWER, Q2_ANSWER = 0, 0
for line in lines:
  Q1_ANSWER += 1 if Q1_SOLUTION(line) else 0
  Q2_ANSWER += 1 if Q2_SOLUTION(line) else 0
print(f"Q1_ANSWER: {Q1_ANSWER}\nQ2_ANSWER: {Q2_ANSWER}")
