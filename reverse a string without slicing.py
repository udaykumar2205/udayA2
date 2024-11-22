#wap to reverse a given string without slicing.
s=input()
rev=' '
for ip in range(-1,-(len(s)+1),-1):
    rev+=s[ip]
