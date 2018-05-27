'''
From given string  s1='I am Mr. X. And I like ice-cream.'
Arrange each word in the string in the descending order of 
number of times of its occurrence. If at any place there is 
degeneracy choose the one with lower index.
'''
import string
s1='I am Mr. X. And I like ice-cream.'
print("Input string= ",s1)
l1=s1.split(' ')
# arrange unique words wrt index and count its frequency 
word=[]
freq=[]
for x in l1:
    if x not in word:
        word.append(x)
        freq.append(l1.count(x))
print(word,'\n',freq)
# sort wrt frequency
final_list=[]
for i in range(len(word)):
    for j in range(len(freq)):
        if freq[j] == max(freq):
            final_list.append(word[j])
            freq[j]=-1
            break
print(final_list)
