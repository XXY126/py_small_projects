count = int(input("QUANTI NUMERI DI FIBONACCI"))

num1 = 1
num2 = 1
temp = num1
i = 1

while i<=count:
    print(num2)
    num2=num2+num1
    num1 = temp
    temp = num2
    i+=1