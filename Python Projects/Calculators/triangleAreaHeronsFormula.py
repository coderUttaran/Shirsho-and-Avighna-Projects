a = int(input("Enter the value of side 1: "))
b = int(input("Enter the value of side 2: "))
c = int(input("Enter the value of side 3: "))
perimeter = a + b + c
s = perimeter/2
area = (s*(s - a)*(s - b)*(s - c))**0.5

print(f"Therefore the area: {area} sq units")