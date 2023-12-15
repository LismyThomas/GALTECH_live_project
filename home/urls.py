from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('cart',views.cart,name='cart'),
    path('student_dashboard',views.student_dashboard,name='student_dashboard'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('student_profile',views.student_profile,name='student_profile'),
    path('course',views.course,name='course'),
    path('student_enrolled_courses',views.student_enrolled_courses,name='student_enrolled_courses'),
    path('login',views.login_view,name='login'),
    path('student_settings',views.student_settings,name='student_settings'),
    path('sign_up',views.sign_up,name='sign_up'),
    path('course_details/<slug:slug>',views.course_details,name='course_details'),
    path('lessons<slug:slug>',views.lessons,name='lessons'),
    path('checkout',views.checkout,name='checkout'),
    path('cart',views.cart,name='cart'),
    
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)