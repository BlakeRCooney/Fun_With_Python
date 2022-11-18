# Ask user for Name

name = input("What is your name?: ")
print(name)

# Ask user for age

age = input("Enter your Age: ")
print(age)

# Ask user for city

city = input("What city do you reside in?: ")
print(city)

# Ask user for what they enjoy

love = input("What activities do you enjoy?: ")
print(love)

# Create output text

string = "Your name is {} and you are {} years old. You live in {} and you love {}."
output = string.format(name,age,city,love)

# Print the output to screen

print(output)
