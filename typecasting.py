# TYPE CASTING IN PYTHON
#
# Type Casting:
# Converting a variable from one data type to another.
#
# There are two types:
# 1. Implicit Type Conversion
# 2. Explicit Type Conversion
#
#
# -----------------------------
# 1. IMPLICIT TYPE CONVERSION
# -----------------------------
#
# a = 10
# b = 2.5
#
# c = a + b
#
# print(c)
# print(type(c))
#
#
# -----------------------------
# 2. EXPLICIT TYPE CONVERSION
# -----------------------------
#
# a = "10"
#
# b = int(a)
#
# print(b)
# print(type(b))
from sysconfig import get_path_names

name = "Anna"
age = 25
gpa = 3.5
is_student = True

print(type (name))
print(type(age))
print(type(gpa))
print(type(is_student))

# Converting
gpa = int(gpa)
print(gpa)

# age = float(age)
# print(age)

# age = str(age)
# print(age)
#
# print (type(age))

name = bool(name)
print(name)

age = bool(age)
print(type(age))