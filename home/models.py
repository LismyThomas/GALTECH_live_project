from django.db import models
from django.contrib.auth.models import User
import os
import uuid
from autoslug import AutoSlugField




# Create your models here.
def unique_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('media', filename)

              
    
class UsersProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
   
    profile_picture = models.ImageField(
        upload_to=unique_name,
        blank=True,
        null=True, 
        default='profile_pics/avatar.png'
    )
    
    
    create_at = models.DateField(null=True, blank=True, auto_now=True)
    update_at = models.DateField(null=True, blank=True, auto_now=True)
    delete_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username



course_choices=[
        (True, 'Paid'),
        (False, 'Unpaid'),
    ]

course_status_choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
]
       
class courses(models.Model):
    course_name=models.CharField(max_length=250)
    course_fee=models.CharField(max_length=50)
    course_description=models.TextField(blank=True, null=True)
    course_type=models.BooleanField(choices=course_choices, default=False)
    course_status=models.CharField(max_length=10, choices=course_status_choices, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(unique=True, populate_from='course_name', default=course_name)
    
   
    course_img = models.ImageField(
        upload_to=unique_name,
        blank=True,
        null=True, 
        default='profile_pics/avt.jpg'
    )
     

    
    def __str__(self):
        return self.course_name
    
    
class Lessons(models.Model):
    
    lesson_title = models.CharField(max_length=50)
    course = models.ForeignKey('Courses', on_delete=models.CASCADE)
    lesson_order = models.IntegerField()

    def __str__(self):
        return self.lesson_title
 
class Video(models.Model):
    video_title = models.CharField(max_length=50)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    thumbnail = models.CharField(max_length=250, help_text='Thumbnail location name')
    video_upload_url = models.CharField(max_length=250, help_text='Video url')
    note = models.TextField(blank=True, null=True)
    video_file = models.CharField(max_length=250, help_text='Video location name')
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.video_title

    
class Reviews(models.Model):  
    course = models.ForeignKey(courses, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    review_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"Review #{self.id} for {self.course.course_name} by {self.user.username}"    


