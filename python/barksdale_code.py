def decode(input_str):
    switcher = {
        '0': '5',
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
    }
    result = ''
    for dig in input_str:
        result += switcher.get(dig)
    return result

decode('4103432323')