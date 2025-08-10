number = int(input("Enter a number: "))

# Convert number to string to find length
num_str = str(number)
length = len(num_str)

# Initialize sum
sum = 0

# Calculate the sum of digits raised to the power of length
temp = number
while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10

# Check if the number is a Weak Armstrong number
if sum == number:
    print(number, "is a Weak Armstrong number")
else:
    print(number, "is not a Weak Armstrong number")