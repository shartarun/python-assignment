#take input from user 
age=int(input("enter your age"))


if(age<18):
    differ=18-age
    print("you are not eligble, wait for", differ,  "more than year"  )
else:
    print("your are eligble")