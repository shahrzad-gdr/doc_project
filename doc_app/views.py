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




"""
=========================================================================================
    show studying students
=========================================================================================
"""
def studying(request):

    queryset = Result.objects.filter(status='E')

    context = {
        'list' : queryset,
    }
    return render(request, 'doc_app/studying.html', context)




"""
=========================================================================================
    create file
=========================================================================================
"""
def crate_certification(request, id):
    url = request.META.get('HTTP_REFERER')

    this_student = Result.objects.get(submitted_course__student__student_id=id)

    path = 'media/'
    doc = DocxTemplate(path + "certificate_temp.docx")

    image_data = open(this_student.submitted_course.course.academy.logo.path, 'rb').read()


    context = {
        'student': this_student.submitted_course.student.first_name + ' ' + this_student.submitted_course.student.last_name ,
        'course': this_student.submitted_course.course.academy.name,
        'academy': this_student.submitted_course.course.name,
        'date': this_student.graduation_date,
        'logo': InlineImage(doc, BytesIO(image_data)),
        'gender': this_student.submitted_course.student.get_gender_display(),

    }

    doc.render(context)
    doc.save('media/certificate/' + f"{this_student.id}.docx")

    this_student.certificate_file = 'media/certificate/' + f"{this_student.id}.docx"
    this_student.save()

    return redirect(url)