lst_m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9], [10, 11, 12, [13, 56, 67, 78]]]

print(lst_m[2][2])

for lst in lst_m:
    for element in lst:
        print(element)

print(lst_m[1].pop(0))

print(lst_m)

def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    
    return result
    
print(flatten(lst_m))