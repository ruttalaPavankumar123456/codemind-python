x=str(input())
vowel=['a','e','i','o','u']
digits=['0','1','2','3','4','5','6','7','8','9']
space=' '
v=c=d=s=0
for i in range (len(x)):
    if x[i] in vowel:
       v+=1
    elif x[i] in digits:
        d+=1
        
    elif x[i] in space:
        s+=1
    else:
        c+=1
print("Vowels:", v) 
print('Consonants:', c)
print("Digits:", d)
print('White spaces:', s)