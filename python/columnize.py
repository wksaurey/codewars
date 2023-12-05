from math import ceil
def columnize(items, columns_count):
    columns = []
    columns_length = [0 for i in range(columns_count)]
    print(columns_length)
    for index in range(len(items)):
        columns[index%columns_count].append(items[index])
    for column_index in range(len(columns)):
        for item in columns[column_index]:
            if len(item) > columns_length[column_index]:
                columns_length[column_index] = len(item)
    print_columns(columns, columns_length, ceil(len(items)/columns_count))

def print_columns(columns, columns_length, column_length):
    result = ''
    for row_index in range (column_length):
        for column_index in (columns_length):
            if column_index > 1: result = result + '|'
            result = result + format()

columnize([1, 123, 123456, 123, 43, 542], 3)