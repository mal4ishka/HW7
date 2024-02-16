import faker
from random import randint
from connect_db import session
from models import Group, Student, Teacher, Subject, Grade

NUMBER_OF_STUDENTS = 50
NUMBER_OF_GROUPS = 3
NUMBER_OF_SUBJECTS = 10
NUMBER_OF_TEACHERS = 5
NUMBER_OF_GRADES = NUMBER_OF_STUDENTS * 20


def generate_fake_data(number_of_groups, number_of_students, number_of_teachers, number_of_subjects,
                       number_of_grades) -> tuple:
    fake_groups = []
    fake_students = []
    fake_subjects = []
    fake_teachers = []
    fake_grades = []
    '''Візьмемо три компанії з faker і помістимо їх у потрібну змінну'''
    fake_data = faker.Faker()

    for _ in range(number_of_groups):
        fake_groups.append(fake_data.pyint())

    for _ in range(number_of_students):
        fake_students.append(fake_data.name())

    for _ in range(number_of_teachers):
        fake_teachers.append(fake_data.name())

    for _ in range(number_of_subjects):
        fake_subjects.append(fake_data.job())

    for _ in range(number_of_grades):
        fake_grades.append(randint(1, 100))

    return fake_groups, fake_students, fake_teachers, fake_subjects, fake_grades


if __name__ == "__main__":
    groups, students, teachers, subjects, grades = generate_fake_data(NUMBER_OF_GROUPS, NUMBER_OF_STUDENTS,
                                                                      NUMBER_OF_TEACHERS, NUMBER_OF_SUBJECTS,
                                                                      NUMBER_OF_GRADES)

    for group in groups:
        row = Group(name=group)
        session.add(row)

    for student in students:
        row = Student(name=student, group_id=randint(1, NUMBER_OF_GROUPS))
        session.add(row)

    for teacher in teachers:
        row = Teacher(name=teacher)
        session.add(row)

    for subject in subjects:
        row = Subject(name=subject, teacher_id=randint(1, NUMBER_OF_TEACHERS))
        session.add(row)

    for grade in grades:
        row = Grade(student_id=randint(1, NUMBER_OF_STUDENTS), subject_id=randint(1, NUMBER_OF_SUBJECTS),
                    grade=grade, timestamp=int(faker.Faker().past_datetime().timestamp()))
        session.add(row)

    session.commit()
    session.close()
