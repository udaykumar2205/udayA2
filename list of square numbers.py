#wap to print list of cube numbers.
l=eval(input())
cube_numbers = []
for i in range(1, 101):
    cube= i ** 3
    cube_numbers.append(cube)  
print(cube_numbers)
