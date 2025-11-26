# 0. Full example
even_message = "an even number: " 
odd_message = "an odd number: "
numbers = range(1, 10)
finished = False

for i in numbers:
    print ("processing number " , i, ", finished: ", finished)
    if i % 2 == 0:
        print (even_message, i)
    else:
        print (odd_message, i)

finished = True
print ("all numbers processed, finished: ", finished)


# 1. User Input
print("Whats your name?") 
input_name = input()
print("Hi 👋", input_name)

# 2. Types
number = 42
print(type(number))
number = "42"
print(type(number))

# 3. Type Conversion
number_as_string = "123"    
number_as_int = int(number_as_string)
print("Number as string: ", number_as_string, ", type: ", type(number_as_string))
print("Number as int: ", number_as_int, ", type: ", type(number_as_int))

number_as_string = "123.45"
number_as_float = float(number_as_string)

# 4. Operators
print("Welt " + "Hallo")
print("Unicredit" * 3)