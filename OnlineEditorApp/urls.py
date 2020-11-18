from django.urls import path
from .import views

app_name = 'OnlineEditorApp'

urlpatterns = [
    path('',views.home, name= 'Home'),
    path('arrays/',views.arrays, name= 'Arrays'),
    path('arrayTraverse/', views.arrayTraverse, name='ArrayTraverse'),
    path('arrayInsertion/', views.arrayInsert, name='ArrayInsertion'),
    path('arrayDeletion/', views.arrayDelete, name='ArrayDeletion'),
    path('arraySearch/', views.arraySearch, name='ArraySearch'),
    path('arrayUpdate/', views.arrayUpdate, name='ArrayUpdate'),
    path('array_IQuestions/', views.arrayIQuestions, name='Array_IQuestions')



]