def find_sum():
    a, b     = 1, 1
    next_num = 2
    sum_even = 0
    while next_num < 4000000:
        if next_num % 2 == 0:
            sum_even += next_num
        a, b = b, next_num
        next_num = a + b
    return sum_even  
