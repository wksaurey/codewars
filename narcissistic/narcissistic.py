

def narcissistic( value ): 
    # find number of digits (7 has one digit, 23 has two, and 153 has 3)
    # separate each digit and multiply it by the number of digits
    # add each multiplication result and return if it equals the original value

    sValue = str(value)
    total = 0
    for i in range (len(sValue)): 
        total += (int(sValue[i]) ** len(sValue))
    return(total == value)

def testNarcissistic ():
    nums = [7, 371, 153, 122, 4887]
    for num in nums:
        if narcissistic(num):
            result = ''
        else: 
            result = "not "
        print(str(num) + " is " + result + "narcissistic")

testNarcissistic()