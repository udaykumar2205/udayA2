#wap to print list of odd numbers.
l=eval(input())
odd_numbers=[]
for i in range(1,101):
    if i%2!=0:
        odd_numbers.append(i)
print(odd_numbers)
