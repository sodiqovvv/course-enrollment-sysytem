# course-enrollment-sysytem
This porject will allow the user to manage course's and student's data in json
----------------------------------------------------------------------------------------------------------------------------------------------------------------
## Process
All students and courses data are stored in "courses_and_students_data.json" file.
First I created 2 classes: Student, and Course.
For each student and course I loaded from json file, I create objects using the classes.
In next step, I linked the objects to each other using list attributes in the classes:
class Course:
    def __init__(self, name, credit, semester):
        self.name = name
        self.credit = credit
        self.semester = semester
     >>>self.students = []<<<
class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.courses = []
     >>>self.tmp_course_names = []<<<
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Here comes the 'Menu':
 Menu:
	1 - Add Student
	2 - Add course
	3 - Enroll student to course
	4 - Unenroll student from course
	5 - Show course info
	6 - Show student info
	7 - Quit
 Enter your choice: 

 1, 2 - These two options are very easy. The program just gets the important input: name, and then finds the object which i stored in a list 

 3, 4 - These ones were a bit tricky. First I had to check whether inputed student and course existed and linked. After that, I again store student object into "students" in Course class and do the same to course objects.

 5, 6 - Pretty easy steps. Just find the objects and printed out.
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
 After the "quit", I have the changes made and simply using for loop and new dictionary, stored them into a "new_file.json" 
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

      
