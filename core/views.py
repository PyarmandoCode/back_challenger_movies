from rest_framework import viewsets,generics
from .models import Movie,Person
from .serializers import PersonSerializer,MovieSerializer,MoviePersonSerializer,PersonMovieSerializer
from rest_framework.permissions import AllowAny


#Esta clase ModelViewset me genera un metodo RESTFULL(get,post,update,delete)
class MovieFullVieSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (AllowAny,)

class PersonFullVieSet(viewsets.ModelViewSet):
    queryset=Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (AllowAny,)

class MoviePersonAll(generics.ListAPIView):
    queryset=Movie.objects.all()
    serializer_class = MoviePersonSerializer
    permission_classes = (AllowAny,)    

class PersonMovieAll(generics.ListAPIView):
    queryset=Person.objects.all()
    serializer_class = PersonMovieSerializer
    permission_classes = (AllowAny,)       