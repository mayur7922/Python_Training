# 1) Write a program to calculate the area and perimeter of different geometric shapes(square, rectangle, parallelogram, triangle, circle) based on user input. The program should include error handling for invalid inputs.

# For square => 

side = int(input("Enter the side length of the square : "))
area = side * side
print("Area of the square is : ", area)

# For rectangle

length = int(input("Enter the length of the rectangle : "))
bredth = int(input("Enter the bredth of the rectangle : "))
area = length * bredth
print("Area of the given rectangle is : ", area)

# 2) Develop a program to take user input for multiple numbers, store them in a list, and compute basic statistical metrics like mean, median, mode, and standard deviation.

# Calculating mean

arr = [];

n = 5;

for i in range(n):
    num = int(input("Enter the value : "))
    arr.append(num)

mean = 0.0;

for i in range(5):
    mean += arr[i]

mean /= n

print("The mean of the array is : ", mean)

# 3) Create a real-world problem-solving program, such as calculating monthly loan payments based on principal, rate of interest, and tenure.