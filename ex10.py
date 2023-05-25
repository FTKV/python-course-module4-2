text = "Hello World"

def split_text(text: str) -> tuple[str, str]:
    first_element = text.split(" ")[0]
    second_element = text.split(" ")[1]
    return first_element, second_element

def split_text(text: str) -> tuple[str, str]:
    result = text.split(" ")
    first_element = result[0]
    second_element = result[1]
    return first_element, second_element

print(split_text(text))

print((0, ))

print(tuple(text))