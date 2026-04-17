nums = []

for i in range(10):
    n = int(input("Введите число: "))
    nums.append(n)

new_list = []

for i in range(len(nums) - 1):
    s = nums[i] + nums[i + 1]
    new_list.append(s)

print(new_list)