
# foreach
# for
# while
# do-while

# input 3 numbers: a, b, c
# until a > b > c
# until sum of all numbers > 100
a = b = c = 0
sum = 0
while True:
    a = int(input("enter A: "))
    b = int(input("enter B: "))
    c = int(input("enter C: "))
    sum = sum + a + b + c
    if a > b and b > c:
        break
    if sum > 100:
        break

