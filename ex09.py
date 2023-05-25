dct = {str(x): x**2 for x in range(10)}

for i in dct:
    print(i)

for i in dct.items():
    print(i)

for i in dct.values():
    print(i)

dct = {str(x): [x]*3 for x in range(10)}

for i in dct:
    print(i)

for i in dct.items():
    print(i)

for i in dct.values():
    print(i)

for key, value in dct.items():
    print(f"{key} - {value}")

for key, value in dct.items():
    print(f"{key} - {sum(value)}")