def valid_braces(user_input):
    while True:
        if '()' in user_input:
            user_input = user_input.replace('()', '')
        elif '{}' in user_input:
            user_input = user_input.replace('{}', '')
        elif '[]' in user_input:
            user_input = user_input.replace('[]', '')
        else: return user_input == ''

print(valid_braces('([{(}])'))
        