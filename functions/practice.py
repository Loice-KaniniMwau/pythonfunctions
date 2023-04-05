##if ,elif,else
def height(myheight):
   if(myheight ==6.1):{
         
        print("you are qualified")
}    
   elif(myheight<6.1):{
        print("you can wait")

}
   else:{
     print("not qualified for the interviw")   
}
def measurements(pi,goldenration):
   if(pi>goldenration):{
         print(f"the {pi}is less than {goldenration}")
   }
   elif pi==goldenration:{
         print(f"the {pi}equals to the {goldenration}")
   }
   else:{
      print("end of the loop")
      }
def age(ages):
   if(ages>6):
      print("you can go to primary school")
   elif ages==5:
      print("you should go to kindergaten")
   else:
      print("you are a baby")
print("done")
def movierating(theNum,moviename):
   print(f"the entered movie rating is :{theNum} ")
   if (theNum>8.5):
      print(f"the movie {moviename} can win the oscars")
   elif theNum<8.5:
      print(f"the fans did not like the plot of {moviename}")
   else:{
         print("the voting has been closed")
   }
print("thank you for participating")      

def studentsRecords(marks ,subject):
    if( marks>=90 and marks<=100):{
   print(f"the student scored A in {subject}")
         }
    elif marks>=80 and marks<=90:
       print(f"the student scored A- in {subject}")
    elif marks>=70 and marks<=80:
       print(f"the student scored B+ in {subject}")
    else:{
          print(f"the student is below the school passmark")
    }
       


   