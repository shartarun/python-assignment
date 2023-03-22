payment=0
total=0
for index in range(3):
    name=input("is there any bike enter name")
    hours=int(input("enter the hours"))
    askUser=input("is there any bike y/n")
    payment=hours*20
    total=payment+total 
    if(askUser=="n"):
        break
print(total)
    
