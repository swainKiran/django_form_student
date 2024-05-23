from django.shortcuts import render, redirect
from app.form import *
from django.http import *
from app.models import *


# #Create your views here.
# def student(request):
#     ESFO=studentInfo()
#     d={'ESFO':ESFO}
#     if request.method == 'POST':
#         SFDO=studentInfo(request.POST)
#         if SFDO.is_valid():
#             print(SFDO.clean_data)
#             return HttpResponse('data submited')
#         else:
#             return HttpResponse('invalid data')    
#     return render(request,'school.html',d)











def insert_Student(request):
    if request.method == 'POST':
        TFDO = studentInfo(request.POST, request.FILES)#request.FILES used for file feteching
        if TFDO.is_valid():
            tn = TFDO.cleaned_data.get('sname')
            sa = TFDO.cleaned_data.get('sage')
            se = TFDO.cleaned_data.get('semail')
            sp = TFDO.cleaned_data.get('spassword')
            ad = TFDO.cleaned_data.get('address')
            hu = TFDO.cleaned_data.get('hubby')
            st = TFDO.cleaned_data.get('school_type')
            sl = TFDO.cleaned_data.get('school_logo')

            # Create a new Student instance
            nm = Student.objects.get_or_create(sname=tn, sage=sa, semail=se, spassword=sp, address=ad, hubby=hu, school_type=st, school_logo=sl)[0]
            nm.save()
            return redirect('student_list')
        else:
            return HttpResponse('invalid data')
    else:
        TFDO = studentInfo()
        d = {'TFDO': TFDO}
        return render(request, 'school.html',d)


def student_list(request):
    SL = Student.objects.all()
    d1 = {'SL': SL}
    return render(request, 'student_list.html',d1)

