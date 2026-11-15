from typing import List

def read_integers() -> List[int]:
    user_input = input()
    input_list = user_input.split(",")
    res = []
    for num in input_list:
        res.append(int(num))
    return res

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
