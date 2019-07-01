
# iterator
for n in range(100, 0, -1):
    print(n)

l1 = list(range(1, 200, 2))
print(l1)

# targil :
# print kfulot 5 100- 500 (kolel)
for n in range(100, 500 + 1, 5):
    print(n)

# print kfulot shel 10 1000-200 yored (kolel)
for n in range(1000, 200 - 1, -10):
    print(n)

# create list numbers odd between 155-300
for n in range(155, 300, 2):
    print(n)

# [5, 8, 10, 200, -30, 50, 300, 2, 0] - print:
#        index 2, 5, 8, ... without knowing len
#          10, 50, 0
l1 = [5, 8, 10, 200, -30, 50, 300, 2, 0, -3]
for n in range(2, len(l1), 3):
    print( l1 [ n ])

# burgers = ['beef', 'chicken', 'veggie', 'Big America']
#   print all the burgers using range
#   print all the burgers reversed using range
#      (without using the reverse command)
#   print the burgers reversed , starting at -1

burgers = ['beef', 'chicken', 'veggie', 'Big America']
#for burger in burgers:
#    print(burger)
for n in range(len(burgers)):
    print(burgers [ n ])

for n in range(len(burgers) - 1, -1, -1):
    print(burgers [ n ])

# etgar
for n in range(-1, -1 * len(burgers) - 1, -1):
    print(burgers [ n ])



