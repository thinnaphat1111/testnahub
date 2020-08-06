def mult_table(from_n, to_n):
    from_n = int (input("เริ่ม = "))
    to_n = int (input("จบ = "))
    for i in range (from_n, to_n + 1 ):
        print("\n")
        for j in range (1, 13):
            print("{} x {} = {} ".format(i, j, i * j))
    for i in range (to_n  , from_n -1 ):
        print("\n")
        for j in range (1, 13):
            print("{} x {} = {} ".format(i, j, i * j))
mult_table("","")