def get_pins(observed): 
    nums = [
        [0, 8], #0
        [1, 2, 4], #1 
        [1, 2, 3, 3], #2
        [2, 3, 6], #3
        [1, 4, 5, 7], #4
        [2, 4, 5, 6, 8], #5
        [3, 5, 6, 9], #6
        [4, 7, 8], #7
        [0, 5, 7, 8, 9], #8
        [6, 8, 9] #9
    ]
    possibilities = list(map(lambda x: nums[int(x)], observed))
    print(possibilities)
    return get_combos(possibilities, 0, 0, [], '')
 
def get_combos(possibilities, digit_index, num_index, results, result):
    if(digit_index >= len(possibilities)): 
        results.append(result)
    elif(num_index >= len(possibilities[digit_index])): 
       return results
    else:
        result += str(possibilities[digit_index][num_index])
        get_combos(possibilities, digit_index+1, num_index, results, result)
        return get_combos(possibilities, digit_index, num_index+1, results, "")
    




print(get_pins('8'))
print(get_pins('11'))
print(get_pins('253'))