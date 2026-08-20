##Exception handling

try:
    a=b
except:
    print("The variable has not been assigned")

try:
    a=b
except NameError as ex:
    print(ex)

try:
    result=1/0
except ZeroDivisionError as ex:
    print(ex)
    print("Please enter the denominator greater than 0")
except Exception as ex1:
    print(ex1)
    print("Main exception got caught here")

try:
    num=int(input("Enter a number"))
    result=10/num
except ValueError:
    print("This is not a valid number")
except ZeroDivisionError:
    print("enter denominator greater than 0")
except Exception as ex1:
    print(ex1)
else:
    print(f"Hey the result is {result}")


#try except else and finally
try:
    num=int(input("Enter a number"))
    result=10/num
except ValueError:
    print("This is not a valid number")
except ZeroDivisionError:
    print("enter denominator greater than 0")
except Exception as ex1:
    print(ex1)
else:
    print(f"Hey the result is {result}")
finally:
    print("Execution complete")

#file hadling and exception handling
try:
    file=open("example1.txt","r")
    content=file.read()
    print(content)
except FileNotFoundError:
    print("The file does not exists")

finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("file close")
