def mult_table(from_n, to_n):
    for i in range (from_n, to_n + 1 ):
        for j in range (1, 13):
            print("{} x {} = {} ".format(i, j, i * j))
mult_table(2,5)