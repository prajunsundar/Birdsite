from django.urls import path
from . import views
app_name='birdapp'

urlpatterns=[
    path('',views.index,name='index'),
    path('details/<slug:b_slug>',views.details,name='details'),
    path('search/',views.search,name='search'),

]
