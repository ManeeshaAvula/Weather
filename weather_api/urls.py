from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("result", views.result, name="result"),
    path('second/',views.second,name='second'),
    # path('social_links', views.social_links),
]
