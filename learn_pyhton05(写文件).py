from sys import argv

script, filename = argv

print("We're going to erase %r" % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that,hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file.  Goodbye!")
target.truncate()

print("now I'm going to ask you for three lines.")

line1=input("line1:")
line2=input("line2:")
line3=input("line3:")

print("I'm going to writing these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally,we close it.")
target.close()
