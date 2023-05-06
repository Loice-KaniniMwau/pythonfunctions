def year_of_birth(name,age):
    year=2023-age
    print(f"hello {name} , you were born in {year}")
    #default arguments
def my_country(country="kenya"):
    print(f"hello you are from {country}")
    ##a function that takes in any numbeer of arguments
    ##positional-written using the asterik to connote possitional arguments
    #takes in a list of numbers /values
def hello(*names):
  for name in names:{
      print(f"hello {name}")   

    }
def sum(*nums):
   answer=0
   for num in nums:
      answer+=num

   return answer
# takes in key word arguments eg a=10,b=20
def multiply_many(**kwargs):
   answer=1
   for num in kwargs.values():
      answer*=num


   return answer  
## Assignment 
# def concatenate_args(*names):
#    first_letter=[]
#    for name in names:
#       first_letter.extend(name)

    
#    return '' .join (first_letter) 
def concetenate(*names):
   first_letter=""
   for name in names:
      first_letter+=name
   return first_letter

def concatenate_kwargs(**many_names):
   first_values=""
   for value in many_names.values():
     first_values+=value
      

   return first_values
##
def mydict(**thedict):
    a={}
    for each in thedict.values():
       key ="somekey"
    a.setdefault(key, [])
    a[key].append([each])
    

    return ''.join (a)
      
      

      
  
          


    
  

     
     
   
       
   