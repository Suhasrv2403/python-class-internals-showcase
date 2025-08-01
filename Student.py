from functools import wraps


class Student:
    """
    A class representing a student with course registration, grade tracking,
    and GPA calculation capabilities. Demonstrates Python internals like
    __slots__, decorators, *args, @property, and rich comparisons.
    """

    # Use __slots__ to save memory and prevent dynamic attribute creation
    __slots__ = ["name", "student_id", "courses", "grades"]

    # Decorator to log method calls with arguments
    def log_calls(func):
        @wraps(func)
        def wrapper(*args):
            print(f"                    -> Logging {func.__name__}" + str(args))
            return func(*args)
        return wrapper

    def __init__(self, name :str, student_id :int):
        """
        Initialize a new student with a name and ID.
        Courses and grades are empty by default.
        """
        self.name = name
        self.student_id = student_id
        self.courses = []
        self.grades = []

    @log_calls
    def register_course(self, *args):
        """
        Register one or more courses for the student.
        Accepts variable number of course names via *args.
        """
        for course_name in args:
            self.courses.append(course_name)

    @log_calls

    def add_grades(self,grade : float):
        """
        Add a grade to the most recently registered course.
        Raises an error if all courses already have grades.
        """

        if len(self.grades) < len(self.courses):
            self.grades.append(grade)
        else:
            raise ValueError("All courses have grades assigned")

    @property
    def gpa(self):
        """
        Compute and return the GPA (average of grades).
        """
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)



    @log_calls
    def __gt__(self, other):
        """
        Compare two students by GPA using 'greater than'.
        """
        if not isinstance(other, Student):
            raise TypeError(f"Cannot compare {type(self)} to {type(other)}")
        return self.gpa > other.gpa

    @log_calls
    def __lt__(self, other):
        """
        Compare two students by GPA using 'less than'.
        """
        if not isinstance(other, Student):
            raise TypeError(f"Cannot compare {type(self)} to {type(other)}")
        return self.gpa < other.gpa

    @log_calls
    def __eq__(self, other):
        """
        Compare two students for GPA equality.
        """
        if not isinstance(other, Student):
            raise TypeError(f"Cannot compare {type(self)} to {type(other)}")
        return self.gpa == other.gpa


    def __str__(self):
        """
        Return a clean string representation of the student,
        including name, ID, courses, grades, and GPA.
        """
        final = ""
        final += f"Name : {self.name}\n"
        final += f"ID : {self.student_id}\n"
        final += f"Courses : {self.courses}\n"
        final += f"Grades : {self.grades}\n"
        final += f"GPA : {self.gpa}"
        return final

if __name__ == "__main__":
    # --- Sample Usage Below ---

    John = Student("John", 1)
    John.register_course("Math")
    John.register_course("Physics")
    John.add_grades(90)
    John.add_grades(80)

    Sarah = Student("Sarah", 2)
    Sarah.register_course("Math")
    Sarah.register_course("Physics")
    Sarah.add_grades(90)
    Sarah.add_grades(80)

    Mike = Student("Mike", 3)
    Mike.register_course("Math")
    Mike.register_course("Physics")
    Mike.add_grades(35)
    Mike.add_grades(60)

    print(John == Sarah) #True
    print(John > Sarah)   #True
    print(Sarah < Mike)   #False