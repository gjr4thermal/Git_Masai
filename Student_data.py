"""stud_no=int(input("enter no of students: "))
stud_name=[] # empty index
for i in range(0,stud_no):
    stud_name[]=input("enter student name: ") # assigning elements in empty index is not possible
print(stud_name)"""

stud_no = int(input("enter no of students: "))
stud_name = [None] * stud_no   # create list with fixed size
stud_data={}
subject=('Maths','Science', 'English')
subject_list=len(subject)

for i in range(stud_no):
    stud_name[i] = input("enter student name: ")
    outer_key=stud_name[i]
    stud_data[outer_key] = {}
    #subject_list = int(input("How many subjects? "))
    
    for j in range(subject_list):
        #subject=input("enter subject: ")
        marks= int(input(f"enter marks for {subject[j]}: "))
        stud_data[outer_key][subject[j]]= marks
        

"""for name, student in stud_data.items():
    total, average=0,0
    total+=sum(student.values())
    average+=total/3
    print(f"total marks of {name} is:",total)
            
"""

print(stud_name)
print(stud_data)
print("\n----- Result -----")

for name, marks_dict in stud_data.items():
    total = sum(marks_dict.values())
    average = total / len(marks_dict)
    
    print(f"Total marks of {name} is: {total}")
    print(f"Average marks of {name} is: {average:.2f}")
    s={'A','B','C'}
    grades=list(s)
    if average>=85:
        print(f"The grade of {name} is: {grades[0]}")
    elif average>=70:
        print(f"The grade of {name} is: {grades[1]}")
    else:
        print(f"The grade of {name} is: {grades[2]}")

    print("-------------------")

#print(f"Average marks of {stud_name} is:",average)
