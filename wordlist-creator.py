from itertools import chain


wordlist = open("wordlist.txt","w")
start_letter = 97

for i in range (0,26):
    for j in range(0,26):
        for k in range(0,26):
            for l in range(0,26):
                for m in range(0,26):
                    string = chr(start_letter+i)+chr(start_letter+j)+chr(start_letter+k)+chr(start_letter+l)+chr(start_letter+m)+"\n"
                    wordlist.write(string)

wordlist.close()