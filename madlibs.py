#python functions recap project
import math


def add(x,y,z):
    print("sum",x+y+z)
    return
add(10,20,30)

def fact(n):

    return(math.factorial(n))


print(fact(4))
print(fact(6))

def student_form():
    institution=(input("Name of institution: "))
    name1=(input("First name: "))
    name2=(input("Second name: "))
    age=(input("Age: "))
    id=(input("Id: "))
    unit=(input("Unit of study: "))
    year=(input("Year: "))
    record=name1,name2,age,id,unit,year,institution
    print( f" Hello {name1} {name2}, your age {age} and Id {id} confirm that you are eligible to join {institution},\n to study {unit} in {year}"  + "\n"
       + str(record))
    return record
student_form()

