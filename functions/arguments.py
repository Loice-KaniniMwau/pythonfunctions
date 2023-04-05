def year_of_birth(name,age):
    year=2023-age
    print(f"hello {name} , you were born in {year}")
def my_country(country="kenya"):
    print(f"hello you are from {country}")
    ##a function that takes in any numbeer of arguments
    ##positional
def hello(*names):
  for name in names:{
      print(f"hello {name}")   

    }
def sum(*nums):
   answer=0
   for num in nums:
      answer+=num

   return answer
def multiply_many(**kwargs):
   answer=1
   for num in kwargs.values():
      answer*=num


   return answer  
## Assignment 
def concatenate_args(*names):
   first_letter=[]
   for name in names:
      first_letter.extend(name)

    
   return '' .join (first_letter) 
def concatenate_kwargs(**many_names):
   first_values=""
   for value in many_names.values():
     first_values+=value
      

   return first_values

      
      

      
  
          


    
  

     
     
   
       
   