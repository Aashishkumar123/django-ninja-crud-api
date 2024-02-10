from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from .models import Student
from .response import response_201
from .schema import StudentSchemaIn, StudentSchemaOut

router = Router()


@router.get("/", response=List[StudentSchemaOut])
def get_students_list(request):
    students = Student.objects.all()
    return students


@router.get("/{student_id}", response=StudentSchemaOut)
def get_student(request, student_id: int):
    student = get_object_or_404(Student, pk=student_id)
    return student


@router.post("/")
def add_student(request, payload: StudentSchemaIn):
    Student.objects.create(**payload.dict())
    return response_201(message="Student created succesfully!!")


@router.patch("/{student_id}")
def update_student(request, studen_id: int, payload: StudentSchemaIn):
    student = get_object_or_404(Student, pk=studen_id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(student, attr, value)
    student.save()
    return response_201(message="Student update succesfully!!")


@router.delete("/{student_id}")
def delete_student(request, studen_id: int):
    student = get_object_or_404(Student, pk=studen_id)
    student.delete()
    return response_201(message="Student deleted succesfully!!")
