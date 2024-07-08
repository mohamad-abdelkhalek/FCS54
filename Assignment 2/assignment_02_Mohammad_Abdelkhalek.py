#####################################
# Mohammad Abdelkhalek Assignment 2 #
#####################################

# Problem 1

list1 = [-11, -4, -1, 2, 4, 5, 7, 11, 19, 25]
start = 0
end = len(list1) - 1
n = 19
    
def binarySearch(list1, start, end, n):
    #Base case
    if start > end:
        print("Element not found")
        return -1
    
    mid = (start + end) // 2
    
    if list1[mid] == n:
        print("Element found at index", mid)
        return mid
    
    elif list1[mid] > n:
        return binarySearch(list1, start, mid - 1, n)
    
    else:
        return binarySearch(list1, mid + 1, end, n)
            
binarySearch(list1, start, end, n)


# Problem 2

characters = ["a", "b", "c"]
n = 2

def printCharacters(characters, n, char=""):
    #Base case
    if(n == 0):
        print(char)
        return   
        
    for i in characters:
        printCharacters(characters, n - 1, char + i)
                    
printCharacters(characters, n)   
            
# Problem 3

def dekenePOS():
    itemsAvailable = [
        {'barcode': 1, 'quantity': 9, 'price': 3.00},
        {'barcode': 2, 'quantity': 15, 'price': 5.50},
        {'barcode': 3, 'quantity': 7, 'price': 12.00},
        {'barcode': 4, 'quantity': 20, 'price': 1.99},
        {'barcode': 5, 'quantity': 3, 'price': 45.00}
    ]

    print("Welcome!")
    receipt = input("Do you want to start a new receipt (yes or no): ")

    def findItem(barcode):
        for item in itemsAvailable:
            if item['barcode'] == barcode:
                return item
        else:
            return None

    if receipt.lower() == "yes":
        itemsForRec = []
        while True:
            barcode = int(input("Enter item barcode: "))
            quantity = int(input("Enter item quantity: "))

            item = findItem(barcode)

            if item and quantity > 0:
                if quantity <= item['quantity']:
                    itemsForRec.append({'barcode': barcode, 'quantity': quantity, 'price': item['price']})
                    item['quantity'] -= quantity
                else:
                    print("Not enough quantity for item with barcode", barcode)
            else:
                print("Invalid barcode or quantity!")

            anotherItem = input("Do you want to add another item to the list? (yes or no): ")
            if anotherItem.lower() != "yes":
                break

        totalCost = sum(item['quantity'] * item['price'] for item in itemsForRec)
        print("Receipt:")
        for item in itemsForRec:
            print("Item barcode:", item['barcode'], "\nQuantity:", item['quantity'], "\nItem price:", item['price'], "\n-----------")
        print("Total cost:", totalCost)

    elif receipt.lower() == "no":
        print("Exiting the system.")

    else:
        print("Please answer with yes or no!")

dekenePOS()
