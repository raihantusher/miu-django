from django.urls import path
from . import views

urlpatterns = [
 path('join-set/',views.join,name="join-set"),
 path('sets/',views.setlist,name="sets"),
 path('set/<str:id>',views.set,name="set"),

 #question list

 path('q/<int:id>', views.question, name="question")
]