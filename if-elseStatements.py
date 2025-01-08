
# Write a program to classify numbers as prime, composite, or neither (for negative or zero values). Ensure it handles invalid inputs gracefully.

def isPrime(n):

    if n <= 1 : return False

    if (n == 2 or n == 3) : return True
    if(n % 2 == 0 or n % 3 == 0) : return False;

    for i in range(5,int(n**0.5) + 1,6) :
        if n % i == 0 :
            return False
        elif n % (i + 2) == 0 :
            return False

    return True;


num = int(input("Enter the number : "))

if num <= 1: 
    print("Neither a prime nor a composite")
elif isPrime(num) == True:
    print("This is a prime number")
else :
    print("This is a composite number")

# Create a program to implement a simple text-based menu system for a library that allows users to add, remove, search, and list books. Use loops and conditional statements effectively.


# Write a robust ATM transaction simulator that includes options for checking balances, depositing, withdrawing money, and exiting. Handle invalid inputs and edge cases.