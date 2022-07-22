# Read dictionary file
f1=open(r'D:\sudhir\basic python\19JUL2022\dictionary.txt','r')
m1=f1.read()
print('dictionary items')
print(m1)
f1.close()

# Read user file
f2=open(r'D:\sudhir\basic python\19JUL2022\sample.txt','r')
m2=f2.read()
print('\nuser paragraph:')
print(m2)
f2.close()
 

# dict convert in list format
dictWords=m1.split('\n')
print('dictWords: ',dictWords)

# userfile convert into list format
userWords=m2.split(' ')

# print('userWords: ',userWords)

# remove \n last element of items

userWords[-1]=userWords[-1].split('\n')
userWords[-1]=userWords[-1][0]
print('userWords: ',userWords)


'''
for dictWord in dictWords:
    print(dictWord)
'''

print("\n dictWords:")
dictWordsLen = len(dictWords)

indx = 0
while indx < dictWordsLen:
    if dictWords[indx] == '':
        dictWords.pop(indx)
        indx -= 1
        dictWordsLen -= 1
    else:
        print(indx, ':', dictWords[indx])
    indx += 1 


print('dictWords: ',dictWords)


# compare list to dict
for userWord in userWords:
    for dictWord in dictWords:
        if userWord==dictWord:
            break
    else:
        print(userWord, 'is not found!')

        # asked to user add to word dictionary yes/no
        add=input("if you want to add word in dictionary (y/n):")
        if add.lower()=='y':
            dictWords.append(userWord)
print(dictWords)

# add to user word in dictionary text file.

f2=open(r'D:\sudhir\basic python\19JUL2022\dictionary.txt','w')
for dictWord in dictWords:
     f2.write(dictWord+"\n")
     
f2.close()
