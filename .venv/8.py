def sort_string(s):
    chars = list(s)
    chars.sort()
    return "".join(chars)

s = input()
print(sort_string(s))
