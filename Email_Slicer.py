# Prompt user for E-mail address

email = input("What is your email address?: ").strip()

# Slice username

user = email[:email.index("@")]

# Slice domain name

domain = email[email.index("@")+1:]

# Format message

output = "Your username is {} and your domain name is {}".format(user, domain)

# Display output message

print(output)
