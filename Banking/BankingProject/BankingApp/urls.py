from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views
app_name='BankingApp'

urlpatterns = [


    path('',views.Home,name='Home'),
    path('login/',views.Login,name='login'),
    path('register/',views.Register,name='register'),

    path('logout/',views.Logout,name='logout'),
    path('application/',views.Apply,name='application'),
    path('applicationsuccess/',views.ApplicationSuccess,name="applicationsuccess"),
]
if settings.DEBUG:
   urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
   urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)