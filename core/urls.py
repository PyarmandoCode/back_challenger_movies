from django.urls import path,include
from . import views
from rest_framework import routers


router=routers.DefaultRouter() # GET,PUT,POST,DELETE
router.register('fullmovies',views.MovieFullVieSet)
router.register('fullpersons',views.PersonFullVieSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('List_Movies_Persons/', views.MoviePersonAll.as_view()),
    path('List_Persons_Movies/', views.PersonMovieAll.as_view()),
]
