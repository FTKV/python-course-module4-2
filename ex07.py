first_people = "Elon Musk"

second_people = "Steve Jobs"

first_set = set("Elon Musk")

second_set = set("Steve Jobs")

print(first_set, second_set)

print(len(first_people) == len(first_set))

print(len(second_people) == len(second_set))

print(first_set & second_set)
print(first_set | second_set)
print(first_set ^ second_set)
print(first_set - second_set)
print(first_set.difference(second_set))