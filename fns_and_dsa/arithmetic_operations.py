def perform_operation(num1, num2, operation):


   if operation == "divide":
      if num2 == 0:
        message = "Zero division error"
        return message
      else:
         result= num1/num2
         return result

   elif operation == "multiply":
      result = num1*num2
      return result
   elif operation == "subtract":
      result = num1- num2
      return result
   elif operation == "add":
      result = num1 + num2
      return result

