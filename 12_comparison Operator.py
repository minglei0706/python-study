#if the temperature is greater than 30
#       it's a hot day
#if the temperature is less than 10
#       it's a cold day
#otherwise
#       it's nether hot or cold

temperature = 30

if temperature >= 30:
    print("It's a hot day")
elif temperature <= 10:
    print("It's a cold day")
else:
    print("It's nether hot or cold")


# if name is less than 3 characters long
#   name must be at least 3 character
# otherwise if it's more than 50 characters long
#   name can be maximum of 50 characters
#  otherwise
#   name looks good!


name = "donner"
name_length = len(name)

if name_length > 50:
    print("name can bi maximum of 50 characters")
elif name_length < 3:
    print("name must be at least 3 characters")
else:
    print("name looks good!")