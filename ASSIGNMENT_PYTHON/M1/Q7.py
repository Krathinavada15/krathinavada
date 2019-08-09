"""7.Write a program to accept a number from the user and determine the sum of digits of that number.
 Repeat the operation until the sum gets to be a single digit number."""

n = int(input("enter n "))
sum = 0
while n!=0:
    sum+=n%10
    n=n//10
print(f"sum of digits is {sum}")
