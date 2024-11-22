#wap to replace all the vowels with there index posit
s=input()
ups=' '
v='aeiouAEIOU'
for ip in range(len(s)):
    if s[ip] in v:
        ups+=str(ip)
    else:
        ups+=s[ip]
    
