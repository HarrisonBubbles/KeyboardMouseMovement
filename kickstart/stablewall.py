import sys

def solve(a, r, c):
    letters = []
    for elem in a:
        if elem not in letters:
            letters.append(elem)
    ans = ""
    while len(ans) != len(letters):
        for letter in letters:
            if letter in ans:
                pass
            else:
                for i in range(len(a)):
                    if i == len(a) - 1:
                       ans = ans + letter
                    elif a[i] != letter:
                        pass
                    elif i > (c * (r - 1) - 1):
                        pass
                    elif letter != a[i + c] and a[i + c] not in ans:
                        break
                if letter == letters[-1] and letter not in ans:
                    return str(-1)
    return ans

T = int(input())
x = []
for j in range(T):
  r, c = map(int, input().split())
  a = []
  for row in range(r):
      a += list(input())
  x.append("Case #" + str(j+1) + ": " + solve(a, r, c))

for elem in x:
    print(elem)
