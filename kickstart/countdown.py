import sys

def solve(a, n, k):
    count = 0
    for i in range(n):
        if i + k > n:
            break
        if a[i] == k:
            for j in range(k):
                if j == 0:
                    pass
                elif j == k - 1 and a[j + i] == 1:
                    count += 1 
                elif a[j + i] == a[j + i - 1] - 1:
                    pass
                else:
                    break
    return str(count)

T = int(input())
x = []
for j in range(T):
  n, k = map(int, input().split())
  a = input().split()
  for i in range(len(a)):
      a[i] = int(a[i])
  x.append("Case #" + str(j+1) + ": " + solve(a, n, k))

for elem in x:
    print(elem)