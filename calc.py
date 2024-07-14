# for first number
while True:
    try:
     num1 = float(input("Enter first number: "))
     break
    except ValueError:
     print("Invalid input. Please enter a number.")
   

# for second number
while True:
         try:
                num2 = float(input("Enter second number: "))
                break
         except ValueError:
                print("Invalid input. Please enter a number.")



try:
      operation=int(input('''enter:
 substraction=1
 addition=2
 division=3
 multiplication=4
    please enter your choice between (1/2/3/4) :
'''))

except ValueError:
 print("enter a valid number")
        
# print(operation)
def sub(num1,num2):
   return num1-num2

def add(num1,num2):
 return num1+num2

def divide(num1,num2):
 if num2 == 0:
    return "Error: Division by zero!"
 else:
  return num1/num2

def multiply(num1,num2):
 return num1*num2


 
if operation==1:
 sub(num1,num2)
 print(f"result of {num1} - {num2}=" ,sub(num1,num2))

elif operation==2: 
 add(num1,num2)
 print (f"result of {num1} + {num2}=" ,add(num1,num2))

elif operation==3:
 divide(num1,num2)
 print(f"result of {num1} \ {num2}=" ,divide(num1,num2))


elif operation==4:
 multiply(num1,num2)
 print(f"result of {num1} x {num2}=" , multiply(num1,num2))

else:
 print("Invalid input. Please enter a valid number (1/2/3/4/).")