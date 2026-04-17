text = []

while True:
    line = input()
    if line == "":
        break
    text.append(line)

text = " ".join(text).lower()

for ch in ",.!?:;-":
    text = text.replace(ch, "")

words = text.split()

counts = {}

for w in words:
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1

result = sorted(counts.items(), key=lambda x: -x[1])

for word, count in result:
    print(word)