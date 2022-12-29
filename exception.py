# print("Start")
# try:
#     print("10/0",10/0)
#     print("After exception line")
# except ZeroDivisionError:
#     print("error when division by zero")   
# print("end of line")

# try:
#     var1=int(input("Enter var-1: "))
#     var2=int(input("Enter Var-2:"))
#     print(var1/var2)
# except ZeroDivisionError:
#     print("division by zero")
# except ValueError:
#     print("only integer")

try:
    f = open('codeTest.csv')
    if f.name != 'codeTest.csv':
        raise IOError 
  
except IOError as e:
    print('file name is not correct!')
except Exception as e:
    print('Second')
else:
    print(f.read())
    
    f.close()
finally:
    print("Executing Finally...")

print('End of program')