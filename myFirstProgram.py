maximum = 0
n = input('Write the amount of numbers: ')
print('Write the numbers: ')
for i in range(int(n)):
    a = input()
    if (int(a) % 5 == 0) and (int(a) > int(maximum)):
        maximum = a

print(maximum)
