# if ,elif,else
# def height(myheight):
#    if(myheight ==6.1):{
         
#         print("you are qualified")
# }    
#    elif(myheight<6.1):{
#         print("you can wait")

# }
#    else:{
#      print("not qualified for the interviw")   
# }
# def measurements(pi,goldenration):
#    if(pi>goldenration):{
#          print(f"the {pi}is less than {goldenration}")
#    }
#    elif pi==goldenration:{
#          print(f"the {pi}equals to the {goldenration}")
#    }
#    else:{
#       print("end of the loop")
#       }
# def age(ages):
#    if(ages>6):
#       print("you can go to primary school")
#    elif ages==5:
#       print("you should go to kindergaten")
#    else:
      # print("you are a baby")
# print("done")
# def movierating(theNum,moviename):
#    print(f"the entered movie rating is :{theNum} ")
#    if (theNum>8.5):
#       print(f"the movie {moviename} can win the oscars")
#    elif theNum<8.5:
#       print(f"the fans did not like the plot of {moviename}")
#    else:{
#          print("the voting has been closed")
#    }
# print("thank you for participating")      

# def studentsRecords(marks ,subject):
#     if( marks>=90 and marks<=100):{
#    print(f"the student scored A in {subject}")
#          }
#     elif marks>=80 and marks<=90:
#        print(f"the student scored A- in {subject}")
#     elif marks>=70 and marks<=80:
#        print(f"the student scored B+ in {subject}")
#     else:{
#           print(f"the student is below the school passmark")
#     }
       
#functions
#even numbers

# def myfun(*nums):
#    for num in nums :
#     if num %2==0:
#            return num

   
    
   #Write a function that takes a list of strings as input and returns a new list with all
   #  strings that contain the letter 'a' removed.
   
def mystrings(stringss):
   strings="aA"
   other_string=""
   for c in stringss:
      if c not in strings:
         other_string+=c
         return other_string

       
stringss=("loice went a to akiraChix"  )
print(mystrings(stringss))
#Write a function that takes a list of numbers as input and returns a 
# new list with all numbers squared.


def numbers(*mynums):
  empty=[]
  empty=[num *num for num in mynums]
  return empty


def eve(*numbers):
   for n in numbers:
      if n%2==0:
         return n
     
def remove_duplicates(*duplicates):
   result=[]
   [result.append(m) for m in duplicates if m not in result] 
   return result
    

remove_duplicates=[1,2,2,3,4,1,5,6]
print(remove_duplicates)

#dictionary comprehension
## calculate the square of each even number from a list and store in dict
numbers = [1, 3, 5, 2, 8]
empty_dict={x:x*x for x in numbers if x%2==0}
print(empty_dict)
#list comprehension
def nums(numbers):
 numbers.sort()
 return numbers
 
numbers=[23,14,76,1,34,19]
print (nums(numbers))
##second largest
def second_largest(mynumbers):
   mynumbers.sort()
   second=mynumbers[-2]
   return second
   
mynumbers=[29,12,1,11,27,8]
print(second_largest(mynumbers))
#smallest element
def smallest_element(numberss):
   numberss.sort()
   smallest=numberss[0]
   return smallest
print(smallest_element(numberss=[23,13,65,98,12,5,45]))

##removing duplicates in a list
def remove_duplicates(duplicated_items):
  result=[]

  [result.append(i) for i in duplicated_items if i not in result]
  return result
duplicated_items=[1,2,3,1,4,5,1,3,2,6,7,8]
print(remove_duplicates(duplicated_items))
#using a set 
# def no_duplicates(*mystring):
#    removing=set (mystring)
#    return list(removing)
# mystring=["loice","jay","faith","lucy","jay","loice"]
# print(no_duplicates(mystring))
   
   #dictionaries
person = {"name": "Jessa", "country": "USA", "telephone": 1178}
print(person.keys())
print(person.values())
print(person.items())
#iterating trhough a dict
for key   in person:
   print(key)
for key_value in person.items():
   print(key_value[0] ,key_value[1])

#adding
person["height"]=5.66
print(person)
person["name"]="loice"
print(person)
#or
person.update({"ID No" : 37220522})
print(person)
#setting default value 





 





   
 
   
   
#Write a function that takes a list of strings as input and returns a new list with all strings capitalized.

# def all_names(*mynames):

 
#Write a function that takes a string as input and returns a new string with all uppercase letters replaced with lowercase letters and all lowercase letters replaced with uppercase letters.
#Write a function that takes a list of numbers as input and returns
#  a new list with all duplicate numbers removed.




   