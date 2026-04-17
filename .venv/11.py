lst = list(map(int, input().split()))
cmd = input()

direction = cmd[0]
k = int(cmd[-1])

k = k % len(lst)

if direction == "R":
    lst = lst[-k:] + lst[:-k]
else:
    lst = lst[k:] + lst[:k]

print(lst)