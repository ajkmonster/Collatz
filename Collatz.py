val = input('Please enter a number: ')
try:
   answer = int(val)
   print("Yes input string is an Integer.")
   print("Input number value is: ", answer)
except ValueError:
   print("That's not an int!")
   print("No.. input string is not an Integer. It's a string")
while answer!=1:
    if answer%2==0:
        answer = answer/2
        print(answer)
    else:
        answer = answer*3+1
        print(answer)
print('Collatz Program has finished')
