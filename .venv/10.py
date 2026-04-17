lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

start = int(input())
end = int(input())

part = lst1[start-1:end]

part.reverse()

lst2.extend(part)

del lst1[start-1:end]

print(lst1)
print(lst2)