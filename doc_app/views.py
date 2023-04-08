from io import BytesIO

from PIL import Image
from django.shortcuts import render, redirect
import qrcode
import qrcode.image.svg
from docxtpl import DocxTemplate, InlineImage

from doc_app.models import Result, Course


"""
=========================================================================================
    show all students
=========================================================================================
"""
def all_students(request):

    queryset = Result.objects.all()

    context = {
        'list' : queryset,
    }
    return render(request, 'doc_app/all_students.html', context)




"""
=========================================================================================
    show all courses
=========================================================================================
"""
def all_courses(request):

    queryset = Course.objects.all()

    context = {
        'list' : queryset,
    }
    return render(request, 'doc_app/courses.html', context)




"""
=========================================================================================
    show graduate students
=========================================================================================
"""
def graduate_students(request):

    queryset = Result.objects.filter(status='G')

    context = {
        'list' : queryset,
    }
    return render(request, 'doc_app/graduate_students.html', context)


