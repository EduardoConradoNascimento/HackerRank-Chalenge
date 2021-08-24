n = int(input("Number to Multiply With While loop:"))

count = 0

while count < 10:
 count += 1
 opperation = n*count
 print(str(n) + " x" + " " + str(count) + " = " + str(opperation))



## Outro jeito de fazer com Py.format

X = int(input("Number to Multiply with For loop:"))

for i in range(1, 11):
    product = n * i
    print ('{} x {} = {}'.format(n, i, product))