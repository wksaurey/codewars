def descending_order(value):
    nums = []
    for num in str(value):
        nums.append(num)
    nums.sort(reverse=True)
    value = ''
    for num in nums:
        value = value + num
    return int(value)

descending_order(185463)