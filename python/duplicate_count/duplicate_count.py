def duplicate_count(text):
    # library of characters, 
    # if exists in library and value duplicate isn't true, 
    # set duplicate to true
    # if duplicate is changed from false to true, update duplicateCount

    text = text.lower()
    chars = {}
    duplicateCount = 0
    for char in text:
        if char not in chars: 
            chars[char] = False
            
        elif chars[char] == False: 
            chars[char] = True
            duplicateCount += 1

    return duplicateCount

duplicate_count("aabcd")
