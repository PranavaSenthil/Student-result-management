from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('vr',views.vr,name='vr'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('dash',views.dash,name='dash'),
    path('sr',views.sr,name='sr'),
    path('semester',views.semester,name='semester'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('subjects',views.subjects,name='subjects'),
    path('edits/<int:id>',views.edits,name='edits'),
    path('deletes/<int:id>',views.deletes,name='deletes'),
    path('students',views.students,name='students'),
    path('editss/<int:id>',views.editss,name='editss'),
    path('deletess/<int:id>',views.deletess,name='deletess'),
    path('results',views.results,name='results'),
    path('eds/<int:id>',views.eds,name='eds'),
    path('dels/<int:id>',views.dels,name='dels'),
]