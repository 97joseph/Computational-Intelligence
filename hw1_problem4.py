# PUT YOUR NAME HERE
# PUT YOUR SBU ID NUMBER HERE
# PUT YOUR NETID (BLACKBOARD USERNAME) HERE
#
# IAE 101 (Fall 2021)
# HW 1, Problem 4

def temp_converter(temperature, f_or_c):
    # ADD YOUR CODE HERE
    f_or_c = f_or_c.lower()
    if f_or_c == "c":
        temperature = 9.0 / 5.0 * temperature + 32
        return "%s degrees Fahrenheit"% temperature
    if f_or_c == "f":
        temperature = (temperature - 32)  / 9.0 * 5.0
        return "%s degrees Celsius"% temperature
 
intemp = int(raw_input("What is the temperature?\n"))
inunit = str(raw_input("Please enter the unit of measure (f or c):\n"))
 
print( temp_converter(intemp, inunit))
   #  return -1 # CHANGE OR REMOVE THIS LINE


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print("temp_converter(100,'C') is", temp_converter(100, 'C'))
    print()
    print("temp_converter(0,'F') is", temp_converter(0, 'F'))
    print()
    print("temp_converter(212,'C') is", temp_converter(212, 'C'))
    print()
    print("temp_converter(32,'C') is", temp_converter(32, 'C'))
    print()
    print("temp_converter(50,'F') is", temp_converter(50, 'F'))
    print()
