from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import Course,Student,EnrolledStudents

def main_page(request):
    return render(request,"main_page.html")


def admin_login(request):
    return render(request, "admin_login.html")

def admin_sucess_login(request):
 us = request.POST.get("a1")
 ps = request.POST.get("a2")
 print(us, ps)
 if us == 'admin' and ps == 'admin':
  return render(request, "admin_page.html")
 else:
  messages.error(request, "invalid username or password")
  return redirect('main')

def schedule_class(request):
    return render(request,"schedule_class.html")

def schedule_sucessfully(request):
    N = request.POST.get("s1")
    Fa = request.POST.get("s2")
    Da = request.POST.get("s3")
    T = request.POST.get("s4")
    Fe = request.POST.get("s5")
    Du = request.POST.get("s6")
    Course(Name=N,Faculty=Fa,Date=Da,Time=T,Fee=Fe,Duration=Du).save()
    return redirect('schedule_class')
def view_all_schedule_classes(request):
    return render(request,"view_all_schedule_classes.html",{"view":Course.objects.all()})
def student_page(request):
    return render(request,"student_page.html")
def student_registeration(request):
    return render(request,"student_registeration.html")
def see_all_available_courses(request):
    return render(request,"see_all_available_courses.html",{"see":Course.objects.all()})
def student_register_sucessfully(request):
    na = request.POST.get("sr1")
    ct = request.POST.get("sr2")
    em = request.POST.get("sr3")
    us = request.POST.get("sr4")
    pas = request.POST.get("sr5")

    Student(Name=na,Contact=ct,Email=em,Username=us,Password=pas).save()
    return redirect('student_registeration')
def student_login(request):
    return render(request,"student_login.html")
def student_login_check(request):
    u = request.POST.get('l1')
    p = request.POST.get('l2')
    try:
      res = Student.objects.get(Username=u,Password=p)
      request.session['user'] = res.No
      request.session['name'] = res.Name
      return render(request,"student_sucessfully_login.html",{"data": res})
    except Student.DoesNotExist:
        messages.error(request,"invalid username or password")
        return redirect('student_login')
def enroll_the_course(request):
 return render(request,"enroll_the_course.html",{"e":Course.objects.all()})

def enroll_successfully(request):
    s_id = request.POST.get("s1")
    s_name = request.POST.get("s2")
    c_name = request.POST.get("s3")
    c_fac = request.POST.get("s4")
    EnrolledStudents(e_id=s_id, e_name=s_name, e_course=c_name, e_faculty=c_fac).save()
    return redirect('view_all_erolled_courses')

def view_all_erolled_courses(request):
    return render(request,"view_all_erolled_courses.html")
def respective_student_enroll_courses(request):
    i = request.GET.get("v1")
    r = EnrolledStudents.objects.filter(e_id =i)
    return render(request,"respective_student_enroll_courses.html",{"st_en":r})
def Cancel_enrolled_courses(request):
    return render(request,"Cancel_enrolled_courses.html",)
def respective_student_cancel_courses(request):
    i = request.GET.get("c1")
    r = EnrolledStudents.objects.filter(e_id=i)
    return render(request,"respective_student_cancel_courses.html",{"st_en":r})
def canceled_courses(request):
    c = request.POST.get("d1")
    f = request.POST.get("d2")
    u = request.POST.get("d3")
    EnrolledStudents.objects.get(e_course=c,e_faculty=f,e_id=u).delete()
    return redirect('view_all_erolled_courses')
def go_and_update_course(request):
    n = request.GET.get("no")
    res = Course.objects.get(No=n)
    return render(request,"go_and_update_course.html",{"up":res})

def updated_course(request):
    name = request.POST.get("u1")
    fac = request.POST.get("u2")
    dat = request.POST.get("u3")
    tim = request.POST.get("u4")
    fe = request.POST.get("u5")
    dur = request.POST.get("u6")
    no = request.POST.get("u7")
    Course.objects.filter(No=no).update(Name=name,Faculty=fac,Date=dat,Time=tim,Fee=fe,Duration=dur)
    return redirect('view_all_schedule_classes')


def go_and_delete_course(request):
    n = request.GET.get("no")
    Course.objects.get(No=n).delete()
    return redirect('view_all_schedule_classes')
