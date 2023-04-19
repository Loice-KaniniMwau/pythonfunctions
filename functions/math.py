# def add(a,b):
#     answer=a+b
#     return answer
# def multiply(a,b,c):
#     product=a*b*c
#     return product
# def subtract(a,b):
#     substraction=a-b
#     return substraction
# def divide(a,b):
#     division=a/b
#     return division
# def remainder(a,b):
#     theremainder=a%b
#     return theremainder

# def sum_multiplication(sum,multiplication):
#     return(f"the  sum is {sum} and the product is {multiplication} ")
# #positional arguments
# print(sum_multiplication(3+4+5+10*2,6*2*10*12*3))

# #default arguments
# def names(firstname="a",secondname="b"):
#     return (f"my name is {firstname}  {secondname}")
# print(names())
# print(names("loice"))
# print(names("kanini","mwau"))
# print(names(secondname="mwau",firstname="kanini"))
#args-positional arguments
def firstname(*names):
    #  for name in names:
    #    print(f'Hello {name}')
  final=[name for name in names]
    
  print(f"hello {final}")

    
    
firstname("kanini","mwau","loice","mary","faith")
## kwargs
def firstname(**kwargs):
    for name in kwargs.values():
        print(name)
      
firstname(a="loice",b="mary",c="kanini")

# def palindrome(names):
#    myname="abc"
#    mysecond="cba"
#    for name in names:
#       if name in myname==name in mysecond:
#          return name
      
# print(palindrome("civic is a radar in kenya"))
# name="kanini"
# print(name[::-1])
# print(name[3::-1])
# print(name[3::])
# print(name[::-2])
# print(name[3::-2])
names="veronica"
print(names[::-1])
print (names[::-2])


##palindrome

def opalindrome(str):
     
         if str==str [::-1]:
             return ("true")
         else:
             return ("false")
         
print(opalindrome("mary"))
#take two
def palindrome(*string):
    finall=[str for str in string]
    if finall==finall[::-1]:
        return ("true")
    else:
        return ("false")

print(palindrome("mary","faith","civic"))
          

         
   
   

 
