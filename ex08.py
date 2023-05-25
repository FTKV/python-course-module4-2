key = "name"
key1 = "title"

lst = ["name", "age", "height"]

if key not in lst:
    print("Yes")
else:
    print("No")

dct = dict.fromkeys(lst, "Klgwjefw")

print(dct)

if key in dct.values():
    print("Yes")
else:
    print("No")

if key in str(dct.values()):
    print("Yes")
else:
    print("No")

if key in str(dct):
    print("Yes")
else:
    print("No")

print(str(dct.values()))

print(str(dct))

if "{" in str(dct):
    print("Yes")
else:
    print("No")