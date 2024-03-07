string=input()
 cnt1=0
 cnt2=0
 for i in string:
     if i.isupper():
         cnt1+=1
     elif i.islower():
         cnt2+=1
 print(cnt1,cnt2)