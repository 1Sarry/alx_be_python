def perform_operation(num1:float, num2:float, operation:str):
#  num1 = int(input ("Enter the first number:"))
#  num2 = int(input("Enter the second number:"))
# operation = input("Choose the operation ('add', 'subtract', 'multiply', 'divide'):")  
   match operation:
      case "divide":
         result= num1/num2
         print(f"The result is {result}")
      case "multiply":
         result= num1*num2
         print(f"The result is {result}")
      case "subtract":
         result= num2 - num1
         print(f"The result is {result}")
      case "add":
         result= num1/num2
         print(f"The result is {result}")