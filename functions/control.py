#creating a range of numbers
#control_flow
def even_numbers():
    x=range(10)
    for i in x :
        if i %2 ==0:
            print (i)
#oodnumbers
def odd_numbers():
    y=range(20)
    for i in y:
        if i %2 !=0:
            print(i)
#else statement
def divisibleby_five():
    x=range(50)
    for i in x :
        if i %5==0:
            print(f"{i} is divisble by 5")
        else:
            print(f"{i} is not divisible by 5")
#elif
def multiple_comparison():
    x=range(50)
    for i in x:
        if i %5==0:
            print(f"{i} is divisible by 5")
        elif i %7==0:
            print(f"{i} is divisble by 7")
        elif i %9==0:
            print (f"{i} is divisible by 9")
        else:
            print(f"{i} is not divisble by 5,7 or 9")
#combining control flow with logical operators
#logical and, or ,not

def divisibleby():
    x=range(50)
    for i in x:
        if i % 5 ==0 and i % 2==0:
            print(f"{i} is divsible by both 5 and 2")
        else:
            print(f"{i}is not divisible by 5 and 2 ")

def odd_or_even():
    x=range(20)
    for i in x:
        if i % 2 ==0 and i % 3==0:
            print(f"{i} is divisible by both 2 and 3")
        elif i % 2==0 or i % 3==0:
            print(f"{i} is divisible by either 2 or 3")
        else:
            print(f"{i} is not divisible by either 2 or 3") 

# while loop
def while_loop():
    x=0
    while x<=10:
        print("hello")
        x+=1 
#break statement-stops the while loop even if the set condition is true
def break_statement():
    x=1
    while x <= 10:
        print("hello")
        x+=1
        if x==5:
            break
#continue statement-skips the remainder of the current iteration and goes to the next iteration
def continue_statement():
    x=0
    while x <=20:
        x+=1
        if x %3==0:
            continue
        print(x)

#Assignment
#Write a function that uses while, if and continue statements to print all
#  the even numbers between 0 and 50.
def even_numbers():
    a=0
    while a < 50:
        a+=1
        if a % 2!= 0:
            continue
    print(a)
#Write a function that takes an integer argument and prints "Prime" 
# if the number is prime, and "Not prime" if the number is not prime.
def prime_numbers(nums):
    # if nums < 1:
    #     print ("num not prime number")
    # else:
    #     for n in range(2,nums):
    #         if (nums % n)==0:
    #             print("num not prime")
    #             break
    #         else

    
         

#Write a function that takes a list of integers as input 
#and prints the sum of all the even numbers in the list.

 def sumofeven_numbers(*mynumbers):
    sum=0
    for i in mynumbers:
        if i %2 ==0:
            sum+=i
    print (sum)
#Write a function that takes any two integers as input, and prints the sum of all the numbers 
# between the two integers (inclusive) that are divisible by 3.
def sumoftwo_numbers(a,b):
    sum=0
    for i in range(a,b+1):
        if i % 3==0:
            sum+=i
    print(sum)

# print all the numbers divisible by 3 using while loop and continue
def divide_by3(a,b):
    for i in range(a,b):
        i+=1
        if(i % 3 !=0):
            print(i)
            continue

# using while
def divide_3():
    start=0
    while(start <=10):
        start+=1
        if(start %3 !=0):
            continue
        print(start)
#sum using a while loop
def sum_of_nums():
    sum=0
    i=0
    while(i <=10):
        sum+=1
        i=i+1
    print(sum)
def while_nums():
    sum=0
    m=0
    while(m<=10):
         sum+=m
         m+=1
    print(sum)
def nums():
    
    starting_num=0
    while(starting_num <=10):
        print(starting_num)
        starting_num+=1
#prime numbers
# def print_primes(numbers):
#     for num in numbers:
#         if num > 1:
#             for i in range(2, num):
#                 if num % i == 0:
#                     break
#             else:
#                 print(num)
def prime_numbers(numbers):
    for num in numbers:
        if num > 1:
            for i in range(2,num):
                if num % i ==0:
                    break
            else:
                print(num)

prime_numbers(numbers=[1,2,4,5,6,7,9,11,13])




         
       
       

  
   



    
    
        



            
















          



