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

#counting values in a lsit and adding them to a dictionary
# def counting(mynames):
#   counted_nums={x: mynames.count(x) for x in mynames}
#   print(counted_nums)
 
# counting(mynames=["loice","loice","faith","mary","loice"])

#take two
def counting_occurrence(nicknames):
  new_counted={}
  for name in nicknames:
   if name in new_counted:
      new_counted[name]+=1
      print(new_counted)
      
   else:
     new_counted[name]=1

   
    
   
counting_occurrence(nicknames=["loice","loice","faith","mary","loice"])

#flattening a 2d array
#sum (+) is used in string concatenation therefore the iterable will
#be the list , then the starting point will be the empty list
def flattening(mylist):
  print(sum(mylist ,[]))

flattening(mylist=[[1,2,3],[15,6,8],[4,6,8]])

#take two
#flattening the list and removing duplicates at the same time
def flatten_list(nestedlist):
  flattened=[]
  for i in nestedlist:
    for j in i:
      if j not in flattened:
        flattened.append(j)
  print(flattened)

flatten_list(nestedlist=[[1,2,3],[15,6,8],[4,6,8]])

#sorting a nested list
def finding_longest(mystrings):
  longest=""
  for i in mystrings:
    if (len(i) > len(longest)):
      longest=i
  return longest

print(finding_longest(mystrings=["loice","jecinta","mary","maryannee"]))

#use list comprehension to find the integers who are larger than the average 
#of the list
def above_avg(integers):
  
  return[i for i in integers if i > (sum(integers)/len(integers))]

print(above_avg(integers=[1,2,3,4,65,34,78]))
#soring a nested list in ascending
def sort_nested(nested_list):
  for i in nested_list:
    for j in i:
     print(sorted())

sort_nested(nested_list=[[4,13,1],[76,23,8],[34,12,67,64]])

#breaking at first occurrence

      

      
  
  
  
   