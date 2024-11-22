#wap to print check the given number is perfect number or not.
n=int(input())
f=1
for i in range(1,n//2+1):
    if n%i==0:
        divisor_sum+=1
if n==divisor_sum:
    print('n is perfect')
else:
    print('n is not perfect')
