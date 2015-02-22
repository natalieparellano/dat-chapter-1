def find_sum():
    a, b     = 1, 1
    next_num = 2
    print 'a is', a
    print 'b is', b
    print 'next is', next_num
    sum_even = 0
    while next_num < 4000000:
        if next_num % 2 == 0:
            print '>>>>> adding', next_num
            sum_even += next_num
        a, b     = b, next_num
        next_num = a + b
        print 'a is', a
        print 'b is', b
        print 'next is', next_num
    return sum_even  


find_sum()
