holes_letters = "abdegopq"
def count_holes(word):
    """Возвращает количество символов с "дырками" в слове."""
    count = 0
    for ch in word:
        if ch in holes_letters:
            count += 1
    return count


text = input()
words = text.split()

holes = 0
no_holes = 0
result = []

for w in words:
    h = count_holes(w)
    holes += h
    no_holes += len(w) - h

    if h >= 2:
        result.append(w)

print(holes, no_holes)
print(result)
