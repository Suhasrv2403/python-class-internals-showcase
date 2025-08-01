# 🎓 Student Management System

A lightweight Python-based system to manage student data, demonstrating key concepts of **Object-Oriented Programming**, **decorators**, **custom comparisons**, **memory optimization with `__slots__`**, and more.

---

## ✅ Features

- Register students with `name` and `student_id`
- Register multiple courses using `*args`
- Add grades with data integrity checks
- Auto-calculate GPA using `@property`
- Memory-efficient object using `__slots__`
- Log method calls using a custom `@log_calls` decorator
- Compare students by GPA using:
  - `__gt__`: Greater than
  - `__lt__`: Less than
  - `__eq__`: Equality

---

## 🧠 Concepts Demonstrated

| Concept          | How It’s Used                               |
|------------------|----------------------------------------------|
| `__slots__`       | Limits instance attributes, saves memory    |
| `*args`           | Allows multiple course registration         |
| Decorators        | Logs method calls                           |
| `@property`       | Dynamically calculates GPA                  |
| Dunder methods    | Custom behavior for `==`, `<`, `>`          |
| OOP Principles    | Encapsulation, abstraction, comparison      |

---

## 🧪 Example Usage

```python
s = Student("John", 1)
s.register_course("Math")
s.register_course("Physics")
s.add_grades(90)
s.add_grades(80)

s1 = Student("John", 1)
s1.register_course("Math", "Physics")
s1.add_grades(90)
s1.add_grades(80)

s2 = Student("John", 1)
s2.register_course("Math", "Physics")
s2.add_grades(35)
s2.add_grades(60)

print(s == s1)  # True
print(s > s2)   # True
print(s < s1)   # False
