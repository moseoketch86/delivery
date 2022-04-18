from django.urls import path
from .import views
# this contains all the aurhentication urls

urlpatterns=[
    path('',views.AuthView.as_view(),name="hello_auth"),
    path('signup/',views.UserSerializer.as_view(),name='sign_up'),

]