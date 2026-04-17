nums = list(map(int, input().split()))

new_nums = []

for n in nums:
    if n != 3:
        new_nums.append(n)

print(new_nums)