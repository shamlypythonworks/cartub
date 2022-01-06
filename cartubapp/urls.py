from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns =[
    path('',views.home,name='home'),
    path('search/',views.searching,name='search'),
    path('contact/',views.contact,name='contact'),
    path('<slug:c_slug>/',views.home,name='filter'),

]
urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
