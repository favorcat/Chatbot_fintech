from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='main'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('reservation/', views.reservation, name='reservation'),
    path('houseKeeping/', views.houseKeeping, name='houseKeeping'),
    path('fbConcierge/', views.fbConcierge, name='fbConcierge'),
]