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

