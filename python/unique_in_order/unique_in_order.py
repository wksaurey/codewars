def unique_in_order(sequence):
    lastLetter = ''
    result = []
    for index, element in enumerate(sequence):
        if element != lastLetter:
            result.append(element)
            lastLetter = element
    print(result)
    return result

unique_in_order('AAABBABC')