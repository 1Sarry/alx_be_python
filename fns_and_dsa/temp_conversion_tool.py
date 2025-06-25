FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp_input =   float(input("Enter the temperature to convert: "))
select_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()


def convert_to_celsius(f_temp):
     temp_in_celsius = (temp_input - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
     print(f"{f_temp}°F is {temp_in_celsius}°C")
     

def convert_to_fahrenheit(c_temp):
     temp_in_fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR * temp_input + 32
     print(f"{c_temp}°C is: {temp_in_fahrenheit}°F")
     

if select_unit == "C":
   temp_in_celsius = convert_to_celsius(temp_input)
elif select_unit == "F":
  temp_in_fahrenheit = convert_to_fahrenheit(temp_input)
else:
   print("Invalid temperature. Please enter a numeric value!")

