Object Oriented Programming
===

Before OOP (Object Oriented Programming), most of our programs were designed around functions aka blocks of statements
which manipulate data. This was is called _procedure-oriented programming_.

Unfortunately, it becomes very complicated to maintain large programs. So OOP techniques emerged.

Principles
---
_Classes and objects_ are the main components of OOP.
    - A class is a new type
    - An object is an instance of a class.
    
For example, int is a type. So in an Object Oriented languages, the int 7 is an object of the class _int_.
In python the method `type` is provided to give the class of an object. (we can also say that is an instance of the
class)

An object/class is composed of:
    - _Fields_: variables that belongs to the class
    - _Methods_: functions of the class.
    
Together, fields and methods are called _attributes_.


A field that belongs to a class is a class variable and a method that belongs to an object is an instance variables.

In python: anatomy of your first class
---
The keyword `class` allows programmer to declare a class.
In python, all class methods have an extra-argument called `self`.

Let's declare a _class_:
```
class Student:
    pass
   
    
>>> s = Student() # creation of a new instance of Student
>>> print(s)
<__main__.Student instance at 0x2323565656>

```

Let's declare a _method_:
```
class Student:
    def say_hi(self):
        print('Hello, how are you?')
   
    
>>> s = Student() # creation of a new instance of Student
>>> s.sayHi() # No self while calling the method sayHi ;-)
Hello, how are you?

```

In python: constructor and object variable
---
A constructor is a method that run as soon as the object is instantiated. It allows developers to do any initialisation
such as initiate object variable. This method is declared as __init__ in python.
```
class Student:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, ny name is %s'% self.name)
   
    
>>> s = Student("Cyril") 
>>> s.sayHi() # 
Hello, ny name is Cyril

```

In python: class variable  
---
Let's declare a class variable and a method using classmethod decorator.
```
class Classroom:

    nb_student = 0
    
     def __init__(self, name):
        self.name = name
        Classroom.nb_student += 1
    
    @classmethod
    def how_many(cls):
        print("We have {:d} students.".format(cls.nb_student))   
```