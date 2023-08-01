# Listing 1.2 Advanced List Features
import sys              # Load the sys module
if len(sys.argv) != 2:  # Check number of command line arguments :
    print("Please supply a filename")
    raise SystemExit(1)
f = open(sys.argv[1])   # Filename on the command line
lines = f.readlines()   # Read all lines into a list
print(sys.argv[0])
print(lines)
f.close()

# Convert all of the input values from strings to floats
fvalues = [float(line) for line in lines]
# fvalues = [float(line) for line in open(sys.argv[1])]

# Print min and max values
print("The minimum value is ", min(fvalues))
print("The maximum value is ", max(fvalues))
