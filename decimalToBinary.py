#Decimal to Binary

#Take the remainder (modulus %) of the number and use the base number
#(base 10 or base 2) to get the correct digit.

x = int(input("Enter a number: "))
output = ""
while (x > 0):
    output = output + str(x % 2)
    x = int(x / 2)

#Reverse the string through slicing
    
output = output[::-1]

print(output)

