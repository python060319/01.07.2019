# foreach - given collection of items
# for - given range

# write progam which accepts numbers
# sum the numbers
# till negative number recieved

sum = 0
number = int(input("Please enter a number\
(negative to exit): "))
while number >= 0:
    sum = sum + number
    if sum > 100:
        break
    number = int(input("Please enter a number\
(negative to exit): "))
print(f'the sum is {sum}')
print('exit loop.....')

# 1
# input numbers until avg > 80
# if negative reciecved break the loop
avg = 0
sum = 0
count = 0
while avg <= 80:
    number = int(input("Please enter a number: "))
    if number < 0:
        break
    if number == 0:
        continue # stops the current iteration
                 # jumps to while condition check
    count = count + 1
    sum = sum + number
    avg = sum / count
    print(f"current avg is {avg}")

print(f"average is {avg}")

# 2
# input numbers till 0 is recieved
# for each number print 1-number range
number = int(input("Please enter a number: "))
while number != 0:
    for n in range(1, number + 1):
        print(n)
    number = int(input("Please enter a number: "))

# given this list:
# [ 1, 5, -6, 2, 55, 0, 'boom', 44]
# go over this list (for or foreach or while)
# print numbers from number to zero (descending)
# ignore negative/zero number (using continue)
# 'boom' breaks the loop
ls1 = [ 1, 5, -6, 2, 55, 0, 'boom', 44]
for number in ls1:
    if number == 'boom':
        break
    if number <= 0:
        continue
    for n in range(number, -1, -1):
        print(n)


