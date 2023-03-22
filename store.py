# writing into invoice
def writeInvoice(fileString):
    # opeing the File
    #print("Writimg invoice")
    fs = open("Invoice.csv", "a")
    #print(fileString)
    fs.write(fileString)
    fs.close()

def listingTheProducts():
    print("Listing the products")
    fs = open("productList.csv", "r")
    print(fs.read())
    fs.close()

def calculatingTotalAmount(quantity, productId):
    #print("Calculating total amount")
    fs = open("productList.csv", "r")
    for fileIndex in fs:
        fileArray = fileIndex.split(",")
        if fileArray[0] == str(productId):
            amount = int(quantity)*int(fileArray[2])
            break
    return amount
    fs.close()

def transctionadd(transactionFileAdd):
    #print("add details in transction file")
    fs=open("transaction.csv", 'a')
    fs.write(transactionFileAdd)
    fs.close()



#def productRead():
#    fs=open("productList.csv", 'r')
#    fs[0]

def autogenerateInvoiceId():
    print("Autogenerating the Invoice Id")

    fs = open("Invoice.csv", "r")
    for fileIndex in fs:
        fileArray = fileIndex.split(',')
        
        
        #print("file Array", fileArray)
    newInvoiceId = int(fileArray[2])+1
    return newInvoiceId
    

# createInvoice function


def createInvoice():
    #print("We are in Create Invoice")
# Asking the customer information from the user
    phoneNumber = input("Please enter customer Phone Number")
    name = input("Enter the customer Name")
    invoiceId = autogenerateInvoiceId()
    fileString = "\n"+name+","+phoneNumber+","+str(invoiceId)
    writeInvoice(fileString)
    listingTheProducts()
    productId = int(input("Enter the product Id"))
    quantity = int(input("Enter the quantity"))
    amount = calculatingTotalAmount(quantity, productId)
    transactionFileAdd= "\n"+str(phoneNumber) + "," + str(productId) + "," + str(quantity) + "," + str(amount)
    totalAmount= 0
    totalAmount=totalAmount + amount
    transctionadd(transactionFileAdd)
    #print(amount)
    for index in range (1000):

        askToUser= input("do you have any produtct Y/N")
    
        if askToUser == "Y":            
            listingTheProducts()
            productId = int(input("Enter the product Id"))
            quantity = int(input("Enter the quantity"))
            amount = calculatingTotalAmount(quantity, productId)
            transactionFileAdd= "\n"+str(phoneNumber) + "," + str(productId) + "," + str(quantity) + "," + str(amount)
            totalAmount=totalAmount + amount
            transctionadd(transactionFileAdd)
        else:
            print("Invoice id and total")
            print("invoice id is ", invoiceId)
            print("total amount is ", totalAmount)
            break
        

   



    #productSno=input("enter a product serial no.")
    #productName=input("enter a product name")
    #unitprice=input("enter a price of proudct")
    #quentityOfProduct=input("enter a quentity of proudct")
    #productstring="\n"+productSno + ","+productName + "," + unitprice + "," + quentityOfProduct
    #productstring="\n"+productSno + ","+productName + "," + unitprice + "," + quentityOfProduct
    #writeProduct(productstring)



# Create Report Function
def createReport():
    print("We are in Create Report")
    #asking the product list from user
    


flagInvoice = input("Is it a new Invoice Y/N?")
if (flagInvoice == "Y"):
    createInvoice()
    
        
else:
    createReport()
