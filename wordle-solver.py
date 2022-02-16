words = open("wordlist.txt","r")
wordlist = words.read()
list = wordlist.split('\n')

supported_chars =['b','y','g']
contin = 'y'

def printList(list):
    for i in range(0,len(list)):
        print(list[i])
    print(len(list))

while(contin == 'y' or contin == 'Y'):
    finalWords = []
    character = input("Enter the characters you know : ")
    
    color = input("Enter the color of the character : ")
    while(color not in supported_chars):
        color = input("Enter the color of the character :")
        if color not in supported_chars :
            print("Not right color")
        else:
            break
    
    if color == 'b':
        for j in range(0,len(list)):
            if character not in list[j]:
                finalWords.append(list[j])
        list = finalWords.copy()
        printList(finalWords)
    
    elif color == 'g':
        finalWords=[]
        pos = int(input("Enter the position of character : "))
        for i in range(0,len(list)):
            try:
                if(list[i].index(character) == pos-1):
                    finalWords.append(list[i])
            except:
                continue
        list = finalWords.copy()
        printList(finalWords)

    elif color == 'y':
        finalWords = []
        pos = int(input("Enter the position of character : "))
        for i in range(0,len(list)):
            try:
                if(list[i].index(character) != pos-1 and character in list[i]):
                    finalWords.append(list[i])
            except:
                continue
        list = finalWords.copy()
        printList(finalWords)
    
    
    contin = input("Continue?[y/n]")