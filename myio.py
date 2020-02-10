#three data types at input 
#string
phrase = input("enter a string")
print("you said" + phrase) #string concatenation
print(f"You said {phrase}") # formatted string litteral

#float

someFloat = float(input("Enter a float: "))
print("you entered Float: " + str(someFloat))
print(f"You entered float: {someFloat}")
#int 
someInt = float(input("Enter an int: "))
print("you entered int: " + str(someInt))
print(f"You entered int: {someInt}")

#string interpolaion is sweet
print(f"Do python in line, like this: {someFloat} * {someInt} = {someFloat * someInt}")
      
