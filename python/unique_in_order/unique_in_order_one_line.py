def unique_in_order(seq):
    return [e for i, e in enumerate(seq) if i == 0 or seq[i-1] != e]

print(unique_in_order('AAABBABC'))
