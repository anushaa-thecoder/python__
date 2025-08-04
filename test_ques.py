from functools import reduce
def sum_of_cubes_positive_odd(numbers): 
    p_odd=filter(lambda a:a>0 and a%2!=0,numbers)
    cube_numbers=map(lambda x:x**3,p_odd)
    return reduce(lambda x,y:x+y,cube_numbers,0)
n=input() 
l=list(map(int,input().split())) 
print(sum_of_cubes_positive_odd(l))



def student_info(students):
    student_dict = {}  
    for name, age in students:
        student_dict[name] = age
    unique_ages =set(student_dict.values())  
    print("Student Dictionary:", student_dict)
    print("Unique Ages:", unique_ages)
student_info([("Jay", 20), ("Aniket", 22), ("Yash", 20), ("Chetan", 21)])