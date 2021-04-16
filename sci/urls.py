from .views import ListViewPage  , first_view , DetailViewPage ,DetailApiView , ListApiView
from django.urls import path

urlpatterns = [
    path('',ListViewPage.as_view(), name = 'index'),
    path('sci/<slug>/',DetailViewPage.as_view() , name = "detail"),
    path('first/',first_view , name = 'first'),
    path('api/',ListApiView.as_view()),
    path('api/<slug>' , DetailApiView.as_view()),

]
app_name = 'sci'