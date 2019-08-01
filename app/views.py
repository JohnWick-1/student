from django.shortcuts import render
from .models import Student
import datetime
import os
# Create your views here.


def home(request):
    date = datetime.datetime.now()
    list_of_student = Student.objects.all()
    last_obj=Student.objects.last().__dict__.get('first_name')
    all_data={'date':date,'last_obj':last_obj,'list':list_of_student}

    return render(request,'app/student_form.html',context=all_data)


def student_save(request):
    date = datetime.datetime.now()
    list_of_student = Student.objects.all()
    last_obj=Student.objects.last().__dict__.get('first_name')
    password=os.urandom(5).hex()
    idt=request.POST['id']

    try:
        id= int(request.POST['id'])

    except:

        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        phone_no = request.POST['phone_nu']
        dob = request.POST['dob']
        country = request.POST['country']

        obj = Student(first_name=first_name, last_name=last_name, phone_nu=phone_no, dob=dob, country=country,
                      status=True, password=password)
        # status add here
        obj.save()
        last_obj = Student.objects.last().__dict__.get('first_name')
        all_data = {'date': date, 'last_obj': last_obj, 'list': list_of_student, 'code': password}
        return render(request, 'app/student_form.html', context=all_data)

    else:

        Student.objects.filter(id=idt).update(first_name=request.POST['firstname'],
                                         last_name=request.POST['lastname'],
                                         phone_nu=request.POST["phone_nu"],
                                         dob=request.POST['dob'],
                                         country=request.POST['country'],
                                         )
        last_obj = Student.objects.last().__dict__.get('first_name')
        all_data = {'date': date, 'last_obj': last_obj, 'list': list_of_student, 'code': password}
        return render(request, 'app/student_form.html', context=all_data)







def update(request,id):
    date = datetime.datetime.now()
    list_of_student = Student.objects.all()
    last_obj=Student.objects.last().__dict__.get('first_name')
    entry = Student.objects.get(id=id)





    all_data = {'date': date, 'last_obj': last_obj, 'list': list_of_student, 'entry':entry}
    return render(request, 'app/student_form.html', context=all_data)


def delete(request,id):
    date = datetime.datetime.now()
    list_of_student = Student.objects.all()
    last_obj=Student.objects.last().__dict__.get('first_name')

    Student.objects.filter(id=id).update(status=False)
    all_data={'date':date,'last_obj':last_obj,'list':list_of_student,}

    return render(request,'app/student_form.html',context=all_data)


def on(request,id):
    date = datetime.datetime.now()
    list_of_student = Student.objects.all()
    last_obj=Student.objects.last().__dict__.get('first_name')
    Student.objects.filter(id=id).update(status=True)
    all_data={'date':date,'last_obj':last_obj,'list':list_of_student,}

    return render(request,'app/student_form.html',context=all_data)

