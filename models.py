from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    students = relationship('Student', back_populates='group')


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    group_id = Column(Integer, ForeignKey(Group.id))

    group = relationship('Group', back_populates='students')
    grades = relationship('Grade', back_populates='students')


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    subjects = relationship('Subject', back_populates='teacher')


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    teacher_id = Column(Integer, ForeignKey(Teacher.id))

    teacher = relationship('Teacher', back_populates='subjects')
    grades = relationship('Grade', back_populates='subject')


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey(Student.id))
    subject_id = Column(Integer, ForeignKey(Subject.id))
    grade = Column(Integer)
    timestamp = Column(Integer)

    students = relationship('Student', back_populates='grades')
    subject = relationship('Subject', back_populates='grades')
