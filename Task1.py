

sentence ="Hello my name is ahmed"
#wordCounter=1 #Counting the first word

#counting the spaces if the words is seperated with space
#for i,char in enumerate(sentence):
#    if char == " ":
#        wordCounter+=1
        
#print(wordCounter)


words=[]
ind=0
vowels={'a':0, 'e':0, 'o':0, 'u':0, 'i':0}
wordCount=0
vowelsCount=0

for i,char in enumerate(sentence):
    if char == " ":
        words.append(sentence[ind:i])
        ind=i+1
    if char in vowels:
        vowelsCount+=1
        vowels[char]+=1
words.append(sentence[ind:])

for element in words:
    if element:
        wordCount+=1

print(wordCount)
print(vowelsCount)
print(vowels)



