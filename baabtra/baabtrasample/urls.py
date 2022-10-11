from django.urls import path
from.import views

urlpatterns=[
    path('home',views.baabtra_home),
    path('courses',views.baabtra_courses),
    path('internship',views.baabtra_internship),
    path('details',views.baabtra_details),
    path('about',views.baabtra_about)
]
