def columnize(items, col_count):
    longest_item = [0 for i in range(col_count + 1)]
    # find longest item for each col
    for item_index in range(len(items)):
        if len(items[item_index]) > longest_item[item_index%col_count]:
            longest_item[item_index%col_count] = len(items[item_index])
    # print items
    result = ''
    extra_space = 1
    for item_index in range(len(items)):
        if item_index%col_count > 0: result = result + '|' + f"{f'{items[item_index]}' : ^{longest_item[item_index%col_count]+2}}"
        else: result = result + f"{f'{items[item_index]}' : <{longest_item[item_index%col_count]+1}}"
        if item_index % col_count == col_count-1: result = result + "\n"

    print(result)
    return result
        
columnize(["1", "12", "123", "1234", "12345", "123456"], 1)
columnize(["1", "12", "123", "1234", "12345", "123456"], 3)
columnize(["1", "12", "123", "1234", "12345", "123456"], 5)
columnize(["1", "12", "123", "1234", "12345", "123456"], 999)
columnize(["", "12", "123", "", "12345", ""], 2)