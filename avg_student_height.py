from traceback import print_tb


stu_height=input("Enter list of height").split()

# converting input to int using for loop 
for i in range(0,len(stu_height)):
    stu_height[i]=int(stu_height[i])

print(f"Height List: {stu_height}")

# for loop for adding height 
total_student=0
total_height=0

for height in stu_height:
    total_height+=height
    total_student+=1

avg_height=round(total_height/total_student)

print(f"Total student :{total_student}")
print(f"Average of height{avg_height}")