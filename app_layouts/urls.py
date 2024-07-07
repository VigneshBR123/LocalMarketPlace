from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.registeration, name='registeration'),
    path('signin/',views.login_page, name='login'),
    path('signout/',views.logout_page, name='logout'),
    path('admin_register/', views.freelancer_register_form2, name='freelancer_register_form2'),
    #path('admin_signup/', views.freelancer_register_form, name='freelancer_register_form'),
    path('professionals/',views.professional,name='professionals'),
    path('specalists/',views.specalists, name='specalists'),
    path('remove_specalist/<str:sid>',views.remove_specalist, name='remove_specalist'),
    path('professionals/<str:Profession_category>',views.professionals_2,name='professionals'),
    path('professionals/<str:cname>/<str:proname>',views.pro_details,name='pro_details'),
    path('addtospecialist/',views.add_to_specialist, name='addtospecialist'),
]

