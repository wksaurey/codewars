def solution(number):
    if number < 3: return 0
    result = 0
    for index in range(number):
        if index % 3 == 0 or index % 5 == 0:
            result += index
    return result