#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/
print("Welcome to the Band Name Generator")

cityname = input("What's the name of the city you grew up in?\n")


petname = input("What's is the name of your favorite pet?\n")

print("You band name could be " + cityname + " " + petname)