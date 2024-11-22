#wap to replace all the digits with h.
s=input()#hello
rev=''
for ch in s:
    if ch.isdigit():
        rev+='H'
    else:
        rev+=ch
print(rev)
