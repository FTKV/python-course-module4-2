# x = 1
# y = 2

# x, y = y, x

# print(x, y)

dct = {str(x): x ** 2 for x in range(1, 11)}

print(dct.get("name"))

print(dct.get("name", "empty string"))