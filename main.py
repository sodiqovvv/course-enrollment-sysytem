from Course import Course
from Student import Student
import json

with open("courses_and_students_data.json") as f:
    my_data = json.load(f)

students_collection = []
courses_collection = []

for s in my_data["students"]:
    name = s["name"]
    group = s["group"]
    courses = s.get("courses", [])
    new_obj = Student(name, group)
    new_obj.tmp_course_names = courses
    students_collection.append(new_obj)

for c in my_data["courses"]:
    name = c["name"]
    credit = c["credit"]
    semester = c["semester"]
    new_obj = Course(name, credit, semester)
    courses_collection.append(new_obj)

course_lookup = {}

for c in courses_collection:
    course_lookup[c.name] = c

for s in students_collection: # obyektlarni bir biriga bog'lash
    for c in s.tmp_course_names:
        course_obj = course_lookup.get(c)
        if course_obj:
            s.courses.append(course_obj)
            course_obj.students.append(s)

while True:
    print(" Menu:\n\t1 - Add Student\n\t2 - Add course\n\t3 - Enroll student to course\n\t4 - Unenroll student from course\n\t5 - Show course info\n\t6 - Show student info\n\t7 - Quit")
    user_input = int(input(" Enter your choice: "))
    print("-"*100)

    match user_input:
        case 1:
            name = input(" Name: ")
            group = input(" Group: ")
            new_obj  = Student(name, group)
            students_collection.append(new_obj)
            print("Student added successfully")
            print("-" * 100)

        case 2:
            name = input(" Name: ")
            credit = int(input(" Credit: "))
            semester = int(input(" Semester: "))
            new_obj = Course(name, credit, semester)
            courses_collection.append(new_obj)
            course_lookup[new_obj.name] = new_obj
            print("Course added successfully")
            print("-" * 100)

        case 3:
            student_name = input(" Student name: ")
            course_name = input(" Course name: ")
            student_obj = False
            for s in students_collection:
                if s.name == student_name:
                    student_obj = s
            course_obj = False
            for c in courses_collection:
                if c.name == course_name:
                    course_obj = c
                    break

            if student_obj and course_obj:
                if course_obj not in student_obj.courses:
                    student_obj.courses.append(course_obj)
                    course_obj.students.append(student_obj)
                    print("Student enrolled successfully")
                    print("-"*100)
                else:
                    print("Student is already enrolled in the course")
                    print("-"*100)
            else:
                print("Course or student not found")
                print("-"*100)

        case 4:
            s_name = input(" Student name: ")
            c_name = input(" Course name: ")
            student_obj = False
            for s in students_collection:
                if s.name == s_name:
                    student_obj = s
                    break
            course_obj = False
            for c in courses_collection:
                if c.name == c_name:
                    course_obj = c
                    break

            if student_obj and course_obj:
                if student_obj in course_obj.students:
                    student_obj.courses.remove(course_obj)
                    course_obj.students.remove(student_obj)
                    print("Successfully unenrolled")
                    print("-"*100)
                else:
                    print("Student was not enrolled")
                    print("-"*100)
            else:
                print("Course or student not found")
                print("-"*100)

        case 5:
            name = input(" Name: ")
            if course_lookup.get(name, False):
                obj = course_lookup[name]
                print(f" Name: {obj.name}")
                print(f" Credit: {obj.credit}")
                print(f" Semester: {obj.semester}")
                print(f" Students: ")
                if obj.students:
                    for s in obj.students:
                        print(f" - {s.name}")
                    print("-"*100)
                else:
                    print("No students")
            else:
                print("Course not found")
                print("-"*100)

        case 6:
            s_name = input(" Name: ")
            student_obj = False
            for s in students_collection:
                if s.name == s_name:
                    student_obj = s
                    break
            if student_obj:
                print(f" Name: {student_obj.name}")
                print(f" Group: {student_obj.group}")
                print(f" Courses:")
                if student_obj.courses:
                    for c in student_obj.courses:
                        print(f" - {c.name}")
                else:
                    print(" - No courses")
                print("-"*100)
            else:
                print("Student not found")
                print("-"*100)

        case 7:
            print("Program finished")
            print("*"*100)
            break

save_data = {
    "students": [],
    "courses": []
}

for s in students_collection:
    tmp_dict = {}
    tmp_dict["name"] = s.name
    tmp_dict["group"] = s.group
    tmp_dict["courses"] = [c.name for c in s.courses]
    save_data["students"].append(tmp_dict)

for c in courses_collection:
    tmp_dict = {}
    tmp_dict["name"] = c.name
    tmp_dict["credit"] = c.credit
    tmp_dict["semester"] = c.semester
    tmp_dict["students"] = [s.name for s in c.students]
    save_data["courses"].append(tmp_dict)

with open("new_file.json", "w") as f:
    json.dump(save_data, f, indent=2)






