from rest_framework import serializers
from .models import Person,Movie

# Proporcione una API REST para acceder a películas y modelos de personas. 

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title','sipnosis','Release_Year','language','genre','top']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields =['lastname','firstname','aliases','typepersona','photo']

#.Los documentos de la película deben incluir referencias o documentos completos a personas en sus diferentes roles.

class MoviePersonSerializer(serializers.ModelSerializer):
    Actor_Actress=PersonSerializer(many=True,read_only=True)
    Director=PersonSerializer(many=True,read_only=True)
    Producer=PersonSerializer(many=True,read_only=True)

    class Meta:
        model=Movie
        fields = ['title','sipnosis','Release_Year','language','genre','top','Actor_Actress','Director','Producer']


#Los documentos de la Persona deben incluir referencias o documentos completos de películas en los diferentes roles que tiene la Persona.        


class PersonMovieSerializer(serializers.ModelSerializer):
    actor_actress=MovieSerializer(many=True,read_only=True)
    director=MovieSerializer(many=True,read_only=True)
    producer=MovieSerializer(many=True,read_only=True)

    class Meta:
        model=Person
        fields =['lastname','firstname','aliases','typepersona','photo','actor_actress','director','producer']
