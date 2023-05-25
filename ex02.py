text = "1234567890"

sum = ""

for i in text:
    if i == "5":
        continue
    sum += i

print(sum)

sum = 0

for i in text:
    sum += int(i)

print(sum)