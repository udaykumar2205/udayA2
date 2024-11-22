#wap to print second even numbers in given range.
ll=int(input())
ul=int(input())
c=0
for i in range(ll,ul+1):
    if i%2==0:
        c+=1
        if c%2==0:
            print(i)
