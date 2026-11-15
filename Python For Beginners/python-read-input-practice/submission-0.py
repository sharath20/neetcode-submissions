def add_two_numbers() -> int:
    res = 0 
    user_input = input()
    int_list = user_input.split(",")
    for i in int_list:
        res += int(i)
    return res


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
