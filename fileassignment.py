
fswrite =open("Feedback.csv", 'a' )
Name=input("Enter a name")
EmailId=input("Enter a Email Id")
PhoneNumber=input("Enter a Phone Number")
Feedback=input("Enter a Feedback")

filestring="\n 1"+","+ Name+","+ EmailId + ","+ PhoneNumber +","+Feedback
print(filestring)
fswrites=fswrite.write("filestring")

print(fswrites)
