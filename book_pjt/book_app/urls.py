from django.urls import path,include
from . import views

urlpatterns = [
   
    path('home',views.home,name='home' ),
    path('register/',views.register,name='register' ),
    path('',views.login,name='login' ),
    path('admin',views.admin,name='admin' ),
    path('logout',views.logout,name='logout' ),
    path('update/<int:pk>/',views.update_book,name='update-books' ),
    path('create/',views.create,name='create' ),

    path('view/<int:id>/',views.view_page,name='view-page'),
]