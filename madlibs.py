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
    record=institution,name1,name2,age,id,unit,year
    print( f" Hello {name1} {name2}, your age {age} and Id {id} confirm that you are eligible to join {institution},\n to study {unit} in {year}"  + "\n"
       + str(record))
    return record
student_form()

def flight_booking():
    airport=(input("AirPort :"))
    social_class=(input("Social Class :"))
    price=int(input("Price :"))
    payment_method=(input("Payment Method"))
    date=(input("Date :"))
    seat=(input("Seat :"))
    expiry="23/09/2021"
    approved:bool=True
    ticket=airport,approved,social_class,price,payment_method,date,approved,seat,expiry
    print(f"Hello,{name},welcome to{airport},you have booked for{social_class},at Ksh{price},through{payment_method} is {approved} \n  your seat number is {seat},your flight is on{date},expiry{expiry}")
    return ticket
flight_booking()