text = input()

for ch in ",.!?:;-":
    text = text.replace(ch, "")

words = text.split()

print(words)