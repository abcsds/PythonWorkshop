def faulty_sum(a, b):
    c = a + b
    if a == 2:
        c = c / 0
    return c
