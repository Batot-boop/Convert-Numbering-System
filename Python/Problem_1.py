def main():
   while True:
       
      # >>>>>>>>> menu_0 that is displayed to the user <<<<<<<<< #
       
       menu_0()
        
      # >>>>>>>>> Check that input only 'A' and 'B' <<<<<<<<< #
       
       while True:
           letter_of_start_or_exit = input("Please enter your choice (A/B): ").upper()
           if letter_of_start_or_exit == "A" or letter_of_start_or_exit == "B":
               break
           else:
               print("Please enter a valid chioce.")

       # >>>>>>>>> Start Program <<<<<<<<< #

       if letter_of_start_or_exit == "A":
           # >>>>>>>>> Check ValueError <<<<<<<<< #
           while True:
                try: 
                  num_of_insert = input("Please insert a number: ")
                  if num_of_insert.isnumeric():
                      number = int(num_of_insert)
                      break
                  else:
                      number = int(num_of_insert,16)
                      break
                except:
                    break
           
          # >>>>>>>>> menu_1 that is displayed to the user <<<<<<<<< #
           
           menu_1()
           
           
           # >>>>>>>>> Check valid choice <<<<<<<<< #
           
           while True:   
                  letter_of_base_from = input("Please enter your choice (A/B/C/D): ").upper()
                  if letter_of_base_from == "A" or letter_of_base_from == "B" or letter_of_base_from == "C" or letter_of_base_from == "D":
                      break
                  else:
                   print("Please enter a valid choice.") 
           
           # >>>>>>>>> Check that input number is base right <<<<<<<<< #
           
           if letter_of_base_from == 'A' and all(c in "0123456789" for c in num_of_insert) == False:  
               print(f"Error: {num_of_insert} is not a valid number on base 10. Please enter a valid number.")
               continue
           elif letter_of_base_from == 'B' and  all(c in "01" for c in num_of_insert) == False:
               print(f"Error: {num_of_insert} is not a valid number on base 2. Please enter a valid number.")
               continue
           elif letter_of_base_from == 'C' and  all(c in "01234567" for c in num_of_insert) == False:
               print(f"Error: {num_of_insert} is not a valid number on base 8. Please enter a valid number.")
               continue
           elif letter_of_base_from == 'D' and  all(c in "0123456789ABDCEF" for c in num_of_insert) == False:
               print(f"Error: {num_of_insert} is not a valid number on base 16. Please enter a valid number.")
               continue
            
           # >>>>>>>>> menu_2 that is displayed to the user <<<<<<<<< #
           
           menu_2()
           
           
           # >>>>>>>>> Check valid choice <<<<<<<<< #

           while True:
               letter_of_base_to = input("Please enter your choice (A/B/C/D): ").upper()
               if letter_of_base_to == "A" or letter_of_base_to == "B" or letter_of_base_to == "C" or letter_of_base_to == "D":
                    break
               else:
                   print("Please enter a valid choice.")
 
           # >>>>>>>>> Conditions for choosing arithmetic operations <<<<<<<<< #
           
           if letter_of_base_from == "A" and letter_of_base_to == "A":
                 print(f"Reslut:  {num_of_insert}")
               
           elif letter_of_base_from == "A" and letter_of_base_to == "B":
                 decimal_binary(num_of_insert)
    
           
           elif letter_of_base_from == "A" and letter_of_base_to == "C":
                 decimal_octal(num_of_insert)
                           
           elif letter_of_base_from == "A" and letter_of_base_to == "D":
                 decimal_hexadecimal(num_of_insert)
           
           elif letter_of_base_from == "B" and letter_of_base_to == "A":
                 print(f"Result:  {binary_decimal(num_of_insert)}")
           
           elif letter_of_base_from == "B" and letter_of_base_to == "B":
                 print(f"Reslut:  {num_of_insert}")
           
           elif letter_of_base_from == "B" and letter_of_base_to == "C":
                 binary_octal(num_of_insert)
           
           elif letter_of_base_from == "B" and letter_of_base_to == "D":
                 binary_hexadecimal(num_of_insert)
           
           elif letter_of_base_from == "C" and letter_of_base_to == "A":
                 print(f"Result:  {octal_decimal(num_of_insert)}")
           
           elif letter_of_base_from == "C" and letter_of_base_to == "B":
                 octal_binary(num_of_insert)
         
           elif letter_of_base_from == "C" and letter_of_base_to == "C":
                 print(f"Reslut:  {num_of_insert}")
           
           elif letter_of_base_from == "C" and letter_of_base_to == "D":
                 octal_hexadecimal(num_of_insert)
           
           elif letter_of_base_from == "D" and letter_of_base_to == "A":
                 print(f"Result: {hexadecimal_decimal(num_of_insert)}")
           
           elif letter_of_base_from == "D" and letter_of_base_to == "B":
                 hexadecimal_binary(num_of_insert)
           
           elif letter_of_base_from == "D" and letter_of_base_to == "C":
                 hexadecimal_octal(num_of_insert)
           
           elif letter_of_base_from == "D" and letter_of_base_to == "D":
                 print(f"Reslut:  {num_of_insert}")  
           
       # >>>>>>>>> End program <<<<<<<<< #

       elif letter_of_start_or_exit == "B":
               print("\nExiting program.\n")
               break 

                  #=========================================== Start Menu Function ===========================================#
               
   # <<<<<<<<<< menu_0 >>>>>>>>> #    

def menu_0():
    print("\n\n** Numbering System Converter **\n")
    print("A) Insert a new number\n")
    print("B) Exit program\n")
   
   # <<<<<<<<<< menu_1 >>>>>>>>> #

def menu_1():
    print("\n\n** Please select the base you want to convert a number from **\n")
    print("A) Decimal\n")
    print("B) Binary\n")
    print("C) Octal\n")
    print("D) Hexadecimal\n")
   
   # <<<<<<<<<< menu_2 >>>>>>>>> #

def menu_2():
    print("\n\n** Please select the base you want to convert a number to **\n") 
    print("A) Decimal\n")
    print("B) Binary\n")
    print("C) Octal\n")
    print("D) Hexadecimal\n")
                        
                  #=========================================== Start transformational functions ===========================================#

   # <<<<<<<<< Decimal >> Binary >>>>>>>>> #

def decimal_binary(num1): 
     Decimal = int(num1)
     Binary = 0
     i = 1
     while Decimal > 0:
         remainder = Decimal % 2
         Binary += remainder * i
         Decimal //= 2
         i *= 10
     print(f"Result:  {Binary}")
    
    # <<<<<<<<< Decimal >> Octal >>>>>>>>> #

def decimal_octal(num1): 
     Decimal = int(num1)
     Octal = 0
     i = 1
     while Decimal > 0:
         remainder = Decimal % 8
         Octal += remainder * i
         Decimal //= 8
         i *= 10
     print(f"Result:  {Octal}")
   
   # <<<<<<<<< Decimal >> Hexadecimal >>>>>>>>> #

def decimal_hexadecimal(num1):
     decimal = int(num1)
     hexadecimal = ""
     hex_digits = "0123456789ABCDEF"
    
     while decimal > 0:
          remainder = decimal % 16
          hexadecimal = hex_digits[remainder] + hexadecimal
          decimal = decimal // 16
    
     print(f"Result:  {hexadecimal}")


   # <<<<<<<<< Binary >> Decimal >>>>>>>>> #

def binary_decimal(num1): 
    num = int(num1)
    dec = 0
    i = 0
    while num > 0:
         digit = num % 10
         dec = dec + digit*(2**i)
         num = num // 10
         i = i + 1
    return dec

   # <<<<<<<<< Binary >> Octal >>>>>>>>> #
   
def binary_octal(num1): 
      binary = int(num1)
      decimal = 0
      power = 0
      while binary != 0:
        decimal += (binary % 10) * (2 ** power)
        binary //= 10
        power += 1
    
      octal = 0
      power = 0
      while decimal != 0:
        octal += (decimal % 8) * (10 ** power)
        decimal //= 8
        power += 1
    
      print(f"Result:  {octal}")

   # <<<<<<<<< Binary >> Hexadecimal >>>>>>>>> #

def binary_hexadecimal(num1): 
    binary = int(num1)
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    decimal = 0
    power = 0
    while binary > 0:
        remainder = binary % 10
        decimal += remainder * (2 ** power)
        binary //= 10
        power += 1
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        decimal //= 16
    print(f"result:  {hexadecimal}")

   # <<<<<<<<< Octal >> Decimal >>>>>>>>> #

def octal_decimal(num1): 
      dec = 0
      i = 0
      while int(num1) > 0:
          digit = int(num1)  % 10
          dec = dec + digit*(8**i)
          num1  = int(num1)  // 10
          i = i + 1
      return dec

   # <<<<<<<<< Octal >> Binary >>>>>>>>> #

def octal_binary(num1): 
    octal = num1
    binary = ""
    for digit in octal:
        decimal = int(digit)
        binary += "{0:03b}".format(decimal)
    print(f"Result:  {binary.lstrip("0")}") 

   # <<<<<<<<< Octal >> Hexadecimal >>>>>>>>> #

def octal_hexadecimal(num1): 
     octal = int(num1)
     hex_digits = "0123456789ABCDEF"
     hexadecimal = ""
     decimal = 0
     power = 0
     while octal > 0:
            remainder = octal % 10
            decimal += remainder * (8 ** power)
            octal //= 10
            power += 1
     while decimal > 0:
            remainder = decimal % 16
            hexadecimal = hex_digits[remainder] + hexadecimal
            decimal //= 16
     print(f"Result:  {hexadecimal}")
 
   # <<<<<<<<< Hexadecimal >> Decimal >>>>>>>>> #
 
def hexadecimal_decimal(num1): 
    conversion_table = {
        '0':0,'1':1,'2':2,'3':3,
        '4':4,'5':5,'6':6,'7':7,
        '8':8,'9':9,'A':10,'B':11,
        'C':12,'D':13,'E':14,'F':15
    }
    position = len(num1)-1
    decimal_number = 0
    for i in num1:
        decimal_number = decimal_number + conversion_table[i] * pow(16 , position)
        position = position - 1
    return decimal_number

   # <<<<<<<<< Hexadecimal >> Binary >>>>>>>>> #

def hexadecimal_binary(num1): 
    hexadecimal = num1
    hex_digits = "0123456789ABCDEF"
    binary = ""
    for digit in hexadecimal:
        decimal = hex_digits.index(digit)
        binary += "{0:04b}".format(decimal)
    print(f"Result:  {binary.lstrip("0")}") 

   # <<<<<<<<< Hexadecimal >> Octal >>>>>>>>> #

def hexadecimal_octal(num1):
    hexadecimal = num1
    octal = ""
    decimal = 0
    power = 0
    for digit in hexadecimal[::-1]:
        decimal += int(digit, 16) * (16 ** power)
        power += 1
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        decimal //= 8
    print(f"Result:  {octal}") 



main()



#Student name(1): Islam Ahmed Salah ID(1): 20230056
#Student name(2): Islam Hassan Jalbee ID(2): 20230059
#Student name(3): Ahmed Hassan Abdel Hamed ID(3): 20230014