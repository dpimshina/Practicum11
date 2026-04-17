text = input()

for ch in ",.!?:;":
    text = text.replace(ch, "")

words = text.split()

unique_words = []

for w in words:
    if w not in unique_words:
        unique_words.append(w)

print(unique_words)