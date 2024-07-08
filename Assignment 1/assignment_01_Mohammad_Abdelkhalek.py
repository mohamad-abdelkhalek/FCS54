#####################################
# Mohammad Abdelkhalek Assignment 1 #
#####################################

# Problem 1

list1 = [54, 76, 2, 4, 98, 100]

int1 = int(input("Enter the first integer: "))
int2 = int(input("Enter the Second integer: "))

def getRange(list1):
    
    for i in list1:
        i = int(i)
        if i > int1 and i < int2:
            print(i)
    
getRange(list1)



# Problem 2

Names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]

def namesContainLetter(Names):
    while True:
        letter = input("Enter a letter: ").lower()
    
        for i in Names:
            if letter in i.lower():
                print(i)
            
namesContainLetter(Names)


# Problem 3

numbers = [-12, 4, 12, 25, 67]

def insertNumber(numbers):
    while True:
        num = int(input("Enter a number (-99 to stop): "))
        
        if(num == -99):
            break
        
        inserted = False
        i = 0
        while i<len(numbers) and inserted == False:
            if numbers[i] > num:
                numbers.insert(i, num)
                inserted = True
            i+=1
            
        if inserted == False:
            numbers.append(num)
                
        print(numbers)
                                
insertNumber(numbers)



# Problem 4

            
Words = """Is this the real life? Is this just fantasy? Caught in a landslide, 
        no escape from reality Open your eyes, look up to the skies and see I'm just 
        a poor boy, I need no sympathy Because I'm easy come, easy go, little high, 
        little low Any way the wind blows doesn't really matter to me, to me Mama, 
        just killed a man Put a gun against his head, pulled my trigger, now he's 
        dead Mama, life had just begun But now I've gone and thrown it all away Mama, 
        ooh, didn't mean to make you cry If I'm not back again this time tomorrow 
        Carry on, carry on as if nothing really matters Too late, my time has come 
        Sends shivers down my spine, body's aching all the time Goodbye, everybody,
        I've got to go Gotta leave you all behind and face the truth Mama, ooh (any
        way the wind blows) I don't wanna die I sometimes wish I'd never been born at
        all I see a little silhouetto of a man Scaramouche, Scaramouche, will you do
        the Fandango? Thunderbolt and lightning, very, very frightening me (Galileo)
        Galileo, (Galileo) Galileo, Galileo Figaro, magnifico But I'm just a poor
        boy, nobody loves me He's just a poor boy from a poor family Spare him his
        life from this monstrosity."""

def printSliceOfWords(Words):
    int1 = int(input("Enter First integer: "))
    int2 = int(input("Enter Second integer: "))
    
    listOfChar = []
    
    if(int1 < 0 or int2 <= 0):
        print("Integer can't be negative!")
        
    elif(int1 > int2):
        print("First integer can't be greater than second one!")
        
    elif(int2 > len(Words)):
        print("Second integer is out of boundaries of the string!")
        
    else:       
        for i in Words:
            listOfChar.append(i)
            
        if(listOfChar[int1-1] == " " and listOfChar[int2+1] == " "):
            word2 = "".join(listOfChar)
            print(word2[int1:int2+1])
        else:
            print("This is not a complete Word!")
       
printSliceOfWords(Words)
            
        


    


