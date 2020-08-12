import random
myrandom = random.randrange(1,7)
while True:
    number=int(input("ป้อนค่า = "))
    if number<0:
        break
    co=(number==myrandom)
    if co:
        print("YES -0-")
        break
    else:
        print("NO T-T")