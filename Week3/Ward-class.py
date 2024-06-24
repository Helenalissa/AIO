from typing import List


class Person:
    def __init__(self, name: str, yob: int):
        self.name = name
        self.yob = yob

    def get_age(self):
        return 2024 - self.yob


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(
            f"Teacher - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.people:
            person.describe()

    def count_doctor(self):
        doctor_count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                doctor_count += 1
        return doctor_count

    def sort_age(self):
        self.people.sort(key=lambda p: p.get_age())

    def compute_average(self):
        teacher_ages = []
        for person in self.people:
            if isinstance(person, Teacher):
                teacher_ages.append(person.yob)
        if not teacher_ages:
            return None
        return sum(teacher_ages) / len(teacher_ages)


student1 = Student("studentA", 2010, "7")
teacher1 = Teacher("teacherA", 1969, "Math")
doctor1 = Doctor("doctorA", 1945, "Endocrinologists")
teacher2 = Teacher("teacherB", 1995, "History")
doctor2 = Doctor("doctorB", 1975, "Cardiologists")

ward1 = Ward("Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

ward1.describe()

print(f"\nNumber of doctors: {ward1.count_doctor()}")

print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()

print(f"\nAverage year of birth (teachers): {ward1.compute_average():.1f}")
