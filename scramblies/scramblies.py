def scramble(s1, s2):
    return all(s1.count(l) >= s2.count(l) for l in set(s2))