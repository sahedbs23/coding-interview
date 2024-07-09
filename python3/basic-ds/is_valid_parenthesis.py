def is_valid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False

    dict = {'(': ')'}
    stack = []

    for character in s:
        if character in dict.keys():
            stack.append(character)
        else:
            print(stack)
            if stack == []:
                return False
            p = stack.pop()
            if character != dict[p]:
                return False

    return stack == []
