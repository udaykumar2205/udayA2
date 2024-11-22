#wap to print alternate even numbers.
ll=int(input())
ul=int(input())
c=0
for n in range(ll,ul+1):
    if n%2==0:
        c+=1
        if c%2!=0:
            print(n)
