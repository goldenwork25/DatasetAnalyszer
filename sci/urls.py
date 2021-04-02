from .views import ListViewPage  , first_view , DetailViewPage 
from django.urls import path

urlpatterns = [
    path('',ListViewPage.as_view(), name = 'index'),
    path('sci/<slug>/',DetailViewPage.as_view() , name = "detail"),
    path('first/',first_view , name = 'first'),

]
app_name = 'sci'