
#Practice Question for Variables and Data Types
def question_1():
    student_name = "Lilly"
    age = 18
    marks = ["75", "60", "65", "85", "90"]

    print(f"{student_name} is {age} and got the following grades {marks}")

def question_2():
    x = "10"
    y = 5
    sum = int(x) + y
    return sum

#Practice questions for conditionals
def pass_or_fail(mark):
    if mark >= 50:
        return "pass"
    else:
        return "fail"
    
def return_pass(marks):
    pass_marks = []
    for i in range(len(marks)):
        if marks[i] >= 50:
            pass_marks += [marks[i]]
            
    return pass_marks



#Practicing loops
def even_or_odd(n):
    i = 1
    while i <= n:
        if i % 2 == 0:
            print(f"{i} is an even number")
        else:
            print(f"{i} is an odd number")
        
        i += 1
        
def pass_or_fail(students):
    for student , mark in students.items():
        if mark >= 50:
            print(f"{student} passed")
            
        else:
            print(f"{student} failed")
students = {
    "Lebo" : 78,
    "Ayesha": 49,
    "Tom": 65
}

#Practicing list and dictionaries
def average(numbers):
    sum = 0
    if len(numbers) == 0:
        return 0
    else:
        for i in numbers:
            sum += i
            
        return sum/len(numbers)

        

def sale(sales):
    profitable_sales = []
    
    for i in sales:
        if i > 900:
            profitable_sales += [i]
            
    return profitable_sales

sales = [1200, 800, 950, 1500, 400]
print(sale(sales))

#functions and logic
def highest_mark(marks):
    
    return

marks = ["75", "60", "65", "85", "90"]
