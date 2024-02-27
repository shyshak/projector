def add_nums(a: float, b: float) -> float:
    return float(a) + float(b)


def substract_nums(a: float, b: float) -> float:
    return float(a) - float(b)


def multuply_nums(a: float, b: float) -> float:
    return float(a) * float(b)


def devide_nums(a: float, b: float) -> float:
    return float(a) / float(b)


print("""This is a simple calc that can add or substract 2 numbers
      Provide your expression below""")
user_input = input().replace(" ", "")

if '+' in user_input:
    first = user_input[:user_input.index('+')]
    second = user_input[user_input.index('+')+1:]
    print(f'The result of adding is {add_nums(first, second)}')
elif '-' in user_input:
    first = user_input[:user_input.index('-')]
    second = user_input[user_input.index('-')+1:]
    print(f'The result of substaction is {substract_nums(first, second)}')
elif '*' in user_input:
    first = user_input[:user_input.index('*')]
    second = user_input[user_input.index('*')+1:]
    print(f'The result of substaction is {multuply_nums(first, second)}')
elif '/' in user_input:
    first = user_input[:user_input.index('/')]
    second = user_input[user_input.index('/')+1:]
    print(f'The result of division is {devide_nums(first, second)}')
