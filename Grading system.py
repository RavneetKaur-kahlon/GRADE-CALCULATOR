print("!!Grade and GPA Calculator!!")
print()
print()
E_marks= int(input("Enter English marks:"))
M_marks= int(input("Enter Maths marks:"))
S_marks=int(input("Enter Science marks:"))
Sc_marks=int(input("Enter Social Science marks:"))
H_marks= int(input("Enter Hindi marks:"))
T_marks= int(input("Total marks of each subject="))
print()
print()
if E_marks > T_marks or M_marks > T_marks or S_marks > T_marks or Sc_marks > T_marks or H_marks > T_marks:
    print("Invalid marks entered!")
else:
    P_= (E_marks + M_marks + S_marks + Sc_marks + H_marks) * 100 / (5 * T_marks)
    print("Percentage =", P_, "%")
print()
print()

if P_ >100:
    print("Invalid")
elif P_<=100 and P_>=90 :
    print ("Grade = A+")
    print("GPA = 4.0")
    print()
elif P_>=85 and P_<90 :
    print ("Grade = A")
    print("GPA = 3.7-4.0")
    print()
elif P_>=80 and P_<85 :
    print ("Grade = A-")
    print("GPA = 3.5-3.7")
    print()
elif P_>=75 and P_<80 :
    print ("Grade = B+")
    print("GPA = 3.3-3.5")
    print()
elif P_>=70 and P_<75 :
    print ("Grade = B-")
    print("GPA = 3.0-3.3")
    print()
elif P_>=65 and P_<70 :
    print ("Grade = C+")
    print("GPA = 2.7-3.0")
    print()
elif P_>=60 and P_<65 :
    print ("Grade = C")
    print("GPA = 2.3-2.7")
    print()
elif P_>=55 and P_<60 :
    print ("Grade = C-")
    print("GPA = 2.0-2.3")
    print()
elif P_>=50 and P_<55 :
    print ("Grade = D+")
    print("GPA = 1.7-2.0 ")
    print()
elif P_>=45 and P_<50 :
    print ("Grade = D")
    print("GPA = 1.3-1.7")
    print()
elif P_>=40 and P_<45 :
    print ("Grade = D")
    print("GPA = 1.0-1.3")
    print()
elif P_>=0 and P_<40 :
    print ("Grade = F")
    print("GPA = 0.0")
    print()
elif P_<0:
    print ("Invalid")

print("--- Result Generated Successfully ---")
    
 
