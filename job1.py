st=input('enter string: ').split()
count=0
for i in st:
    if len(i)>count:
        count=len(i)
        word=i    
print('the longest word is: ',word)
