
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

# input numbers until avg > 80
# if negative reciecved break the loop
