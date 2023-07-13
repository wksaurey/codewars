def valid_parentheses(paren_str):
    paren_count = 0
    for paren_char in paren_str:
        if paren_char == '(': paren_count += 1
        elif paren_char == ')': paren_count -= 1
        if paren_count < 0: return False
        print(paren_count)
    return paren_count == 0

print(valid_parentheses('()(())'))