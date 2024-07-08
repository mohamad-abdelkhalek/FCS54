#####################################
# Mohammad Abdelkhalek Assignment 3 #
#####################################

# Problem 1

list1 = [
  [
    "First Name", "Bob", "Last Name", "Alice", "Job Title", "Instructor","Company", "SE Factory"
  ],
  [
    "First Name", "Anis", "Last Name", "Ismail", "Job Title",
    "Instructor", "Company", "SE Factory"
  ],
  [
    "First Name", "Bob", "Last Name", "Alice", "Job Title", "Instructor","Company", "SE Factory"
  ],
  [
    "First Name", "Manuella", "Last Name", "Germanos", "Job Title",
    "Instructor", "Company", "SE Factory"
  ],
]

def convertToDict(list1):
    userDict = {}
    
    for i in list1:
        curr = iter(i)
        tempDict = {}
        firstName = None
        
        for key in curr:
            value = next(curr)
            
            if key == "First Name" and firstName is None:
                firstName = value
            
            tempDict[key] = value
        
        userDict[firstName] = tempDict
        
    return userDict

finalDict = convertToDict(list1)

for key, value in finalDict.items():
    print(key, ":", value)


# Problem 2

listOfStrings = ["Zebra", "apple", "BeAr"]
list1 = [2, 3, 45, 1, 7, 66, 12, 10, 4]

def insertionSort(arr):
    
    ignoreCase = []

    for i in arr:
        ignoreCase.append(i.lower())
    
    for i in range(1, len(ignoreCase)):
        j = i
        while j > 0 and arr[j-1].lower() > arr[j].lower():
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

insertionSort(listOfStrings)
print(listOfStrings)


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    leftSorted = mergeSort(leftHalf)
    rightSorted = mergeSort(rightHalf)

    return merge(leftSorted, rightSorted)

def merge(left, right):
    sortedArr = []
    leftIndex = 0
    rightIndex = 0

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex].lower() <= right[rightIndex].lower():
            sortedArr.append(left[leftIndex])
            leftIndex += 1
        else:
            sortedArr.append(right[rightIndex])
            rightIndex += 1

    sortedArr.extend(left[leftIndex:])
    sortedArr.extend(right[rightIndex:])

    return sortedArr

print(mergeSort(listOfStrings))


# Problem 3

listOfTuples = [(1,1),(1,10),(2,1),(3,0),(3,1)]

def searchForIndices(listOfTuples, n):
    indices = []
    
    for index, (i, j) in enumerate(listOfTuples):
        if i == n or j == n:
            indices.append(index)
            
    print(indices)

searchForIndices(listOfTuples, 1)

    

            
    