number=int(input("ป้อนค่า = "))
for row in range (number):
    for colum in range (number):
        if row ==0 or row==number-1 or colum==0 or colum==number-1:
            print("X",end="")
        else:
            print(" ",end="")
    print(" ")