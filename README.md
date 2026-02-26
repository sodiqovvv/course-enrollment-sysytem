# course-enrollment-sysytem
This porject will allow the user to manage course's and student's data in json
----------------------------------------------------------------------------------------------------------------------------------------------------------------
## Process
All students and courses data are stored in "courses_and_students_data.json" file.
First I created 2 classes: Student, and Course.
For each student and course I loaded from json file, I create objects using the classes.
In next step, I linked the objects to each other using list attributes in the classes:

```python
class Course:
    def __init__(self, name, credit, semester):
        self.name = name
        self.credit = credit
        self.semester = semester
        self.students = []

class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.courses = []
        self.tmp_course_names = []
