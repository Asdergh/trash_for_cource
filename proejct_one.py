import math as mt
import random as rd
import os
import itertools as itr
import string as st
import json as js




def fibonachi_numbers(numbers_count):

    fib_number = 0
    fib_number_history = []
    
    for curent_number in range(numbers_count):

        if len(fib_number_history) == numbers_count:
            break
        
        if len(fib_number_history) < 3:
            
            fib_number = curent_number
            fib_number_history.append(fib_number)
        
        else:

            fib_number = fib_number_history[curent_number - 1] + fib_number_history[curent_number - 2]
            fib_number_history.append(fib_number)
    
    return fib_number_history

trash_task = fibonachi_numbers(numbers_count=100)
print(f"total count of numbers in sequence: [{len(trash_task)}], values: [{trash_task}]")




def FizzBuzz(max_number):

    for curent_number in range(max_number):

        if (curent_number // 3) == 0:
            print("Fizz")
        
        elif (curent_number // 5) == 0:
            print("Bazz")
        
        else:
            print(f"number: [{curent_number}]")

trash_task_1 = 1200
FizzBuzz(trash_task_1)



# задавать вручную все данный о каждом студенте долго и суть задания в основном в том чтобы по оценке математического ожидения вычислить лучшего стедента что и реализовано
# также я решил что реальзовать небольшой класс будет логичнее нежели просто ообъялять функцию 

class StudentsEstimation():

    def __init__(self, subjects) -> None:
        
        self.subjects = subjects
        self.students_names = ["Rosy", "Billy", "Entony", "Glen", "Paul"]
        self.students_lastname = ["Johnson", "Jones", "Anderson", "Smith", "Brown"]

        self.students_log = {f"{student[0]}, {student[1]}":{subject: rd.randint(0, 10) for subject in self.subjects} for student in itr.product(self.students_names, self.students_lastname)}
    
    def get_average(self):

        self.total_average_grade = 0
        for student in self.students_log.keys():
            self.students_log[student]["avg grade"] = sum(self.students_log[student].values()) / len(self.students_log[student].values())
        
        self.all_avg_grades = [self.students_log[student]["avg grade"] for student in self.students_log.keys()]
        self.total_average_grade = sum(self.all_avg_grades) / len(self.all_avg_grades)

        self.upper_grade_bound = 0
        self.top_student = None

        for student in self.students_log.keys():

            if self.upper_grade_bound < self.students_log[student]["avg grade"]:

                self.upper_grade_bound = self.students_log[student]["avg grade"]
                self.top_student = student
            
            else:
                pass
        
        print(f"\nAll Estimation Results --> \n[{self.all_avg_grades}]\nTotal Estimation Result:\n[{self.total_average_grade}]\nBetter Estimation Result: [student: ({self.top_student}), result: {self.upper_grade_bound}]\n")

trash_task_2 = StudentsEstimation(subjects=["russian language", "math", "theory of fields", "differential equotions", "programming", "varitional calculas"])
trash_task_2.get_average()




# вспонимаем формула гирона S = sqrt(p * (p - a) * (p - b) * (p * c))
# где p = a + b + c

def calculate_square(*sides):

    if len(sides) > 3:

        raise ValueError("too many sides for triangle, must be 3")
    
    if (sides[0] + sides[1] > sides[2]) or (sides[0] + sides[2] > sides[1]) or (sides[2] + sides[1] > sides[0]):

        p = sides[0] + sides[1] + sides[2]
        square = mt.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))
        
        return square

    else:

        raise ValueError("must accept by the triangle existance rool")
    
    

trash_task_3 = calculate_square(1, 2, 3)
print(trash_task_3)





def EratoswenMethod(init_number):

    numbers = [number + 1 for number in range(init_number)]
    curent_label = 0

    for number in numbers:

        curent_label = number
        for label_del in range(len(numbers)):
            
            try:

                if (numbers[label_del] // curent_label) == 0:
                    numbers.pop(label_del)
                
                else:
                    pass

            except BaseException:
                pass
    
    return numbers

trash_task_4 = EratoswenMethod(20)
print(trash_task_4)



#высчитывать весь файл долго поэтому я считываю только 100000 первых символов для получения частот присутствия каждого символа
def file_stat(file_name):

    with open(file_name, "r") as file:
        
        file_string = file.read()[:100000]
        simbols_log = {simbol: file_string.count(simbol) / len(file_string) for simbol in file_string if simbol not in st.printable}
    
    return simbols_log



simbols_log = file_stat("war_and_peace.txt")
print(simbols_log)




def calculator(samples_file):

    with open(samples_file, "r") as file:

        samples = file.readlines()
        calculated_values = []
        for sample in samples:

            sample_members = sample.split()
            curent_value = None

            for member in range(len(sample_members)):
                   
                
                print(sample_members[member])

                try:

                    if sample_members[member] == "+":
                            
                        curent_value += float(sample_members[member + 1])
                        print(f"curent_value: {curent_value}")
                        
                    elif sample_members[member] == "-":

                        curent_value -= float(sample_members[member + 1])
                        print(f"curent_value: {curent_value}")
                        
                    elif sample_members[member] == "/":

                        curent_value / float(sample_members[member + 1])
                        print(f"curent_value: {curent_value}")
                        
                    elif sample_members[member] == "*":

                        curent_value *= float(sample_members[member + 1])
                        print(f"curent_value: {curent_value}")
                        
                    elif sample_members[member] == "**":

                        curent_value = curent_value ** float(sample_members[member + 1])
                        print(f"curent_value: {curent_value}")

                        
                    else:
                        
                        print("check", sample_members[member])
                        curent_value = float(sample_members[member])
                        print(f"curent_value: {curent_value}")
                
                except BaseException:
                    pass
        

            calculated_values.append(curent_value)
    
    return calculated_values


trash_task_5 = calculator("samples.txt")
print(trash_task_5)
                
