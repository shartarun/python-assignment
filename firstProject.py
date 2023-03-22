
#Take input form user A Number
firstNumber=int(input("Enter a first integer number "))
secondNumber=int(input("Enter a second integer number "))
#check the input is integer or not
print(type(firstNumber))
print(type(secondNumber))

#check the input is even or odd
if firstNumber and secondNumber % 2 == 0:
    print("firstNumber is even")
    sum=firstNumber + secondNumber
    print("Sum of first and second number : ", sum)

else:
    print("firstNumber is odd ")
    product=firstNumber * secondNumber
    print("Product of first and second number : ", product)




