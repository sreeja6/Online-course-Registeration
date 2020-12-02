"""sessions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main_page,name='main'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_sucess_login/', views.admin_sucess_login, name='admin_sucess_login'),
    path('schedule_class/',views.schedule_class,name='schedule_class'),
    path('schedule_sucessfully/',views.schedule_sucessfully,name='schedule_sucessfully'),
    path('view_all_schedule_classes', views.view_all_schedule_classes, name='view_all_schedule_classes'),
    path('student_page/',views.student_page,name='student_page'),
    path('student_registeration/',views.student_registeration,name='student_registeration'),
    path('see_all_available_courses/',views.see_all_available_courses,name='see_all_available_courses'),
    path('student_register_sucessfully/',views.student_register_sucessfully,name='student_register_sucessfully'),
    path('student_login/', views.student_login, name='student_login'),
    path('student_login_check/', views.student_login_check, name='student_login_check'),
    path('enroll_the_course/',views.enroll_the_course,name='enroll_the_course'),

    path('enroll_successfully/',views.enroll_successfully,name='enroll_successfully'),
    path('view_all_erolled_courses/',views.view_all_erolled_courses,name='view_all_erolled_courses'),
    path('respective_student_enroll_courses/',views.respective_student_enroll_courses,name='respective_student_enroll_courses'),
    path('Cancel_enrolled_courses/',views.Cancel_enrolled_courses,name='Cancel_enrolled_courses'),
    path('respective_student_cancel_courses/',views.respective_student_cancel_courses,name='respective_student_cancel_courses'),
    path('canceled_courses/',views.canceled_courses,name='canceled_courses'),
    path('go_and_update_course/',views.go_and_update_course,name='go_and_update_course'),
    path('updated_course/',views.updated_course,name='updated_course'),
    path('go_and_delete_course/',views.go_and_delete_course,name='go_and_delete_course')

]

