# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

#int.input to int(input)
#("Greetings! What is your year of origin? ') to ("Greetings! What is your year of origin? ""))
year = int(input("Greetings! What is your year of origin? "))

#Colon added
#backslash added at that's
if year <= 1900:
    print ("Woah, that's the past!")
elif  1900 < year < 2020:
    print ("That's totally the present!")
else: #else instead of elif
    print ("Far out, that's the future!!")
