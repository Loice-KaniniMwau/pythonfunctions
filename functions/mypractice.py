def mystrings(stringss):
   strings="aA"
   other_string=""
   for c in stringss:
      if c not in strings:
         other_string+=c
   return other_string

       
stringss=("aloAice went a tao akiraChix"  )
final=mystrings(stringss)
print(final)
# Write a function that takes a list of strings as input 
# and returns a new list with all strings capitalized.
def capital(string_list):
 return[string.upper() for string in string_list]

string_list=["loice","kanini","mary","macian"]
print(capital(string_list))

# Write a function that takes a string as input and returns a new string with all uppercase letters replaced with lowercase letters and
#  all lowercase letters replaced with uppercase letters.


# Write a function that takes a list of numbers as input and 
# returns a new list with all numbers squared.
def numbers(numbs):
   return[num*num for num in numbs]

numbs=[1,2,3,4,5,6]
print (numbers(numbs))
#Write a function that takes a list of numbers as input and 
# returns a new list with all duplicate numbers removed.
def duplicate(mynums):
 empty=set(mynums)
 return list(empty)
    

mynums=[1,2,1,3,4,2,4,5]
print(duplicate(mynums))
