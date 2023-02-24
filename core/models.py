from django.db import models


class TypePerson(models.Model):
    type_person = (
        ('Actor_Actress','Actor_Actress'),
        ('Director','Director'),
        ('Producer','Producer'),
        ('Extras','Extras'),
    )
    type_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=15,choices=type_person)
    state=models.BooleanField(default=True)
    created_at=models.DateTimeField('created_at',auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name='TypePerson'    
        verbose_name_plural='TypePersons'    
        ordering=['type']


class Person(models.Model):
    person_id =models.AutoField(primary_key=True)
    lastname = models.CharField(max_length=180)
    firstname = models.CharField(max_length=180)
    aliases =models.CharField(max_length=80,blank=True,null=True)
    photo = models.CharField(max_length=180,blank=True,null=True)
    typepersona=models.ForeignKey(TypePerson,on_delete=models.CASCADE,related_name='person') 
    state=models.BooleanField(default=True)
    created_at=models.DateTimeField('created_at',auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.lastname,self. firstname)

    class Meta:
        verbose_name='Person'    
        verbose_name_plural='Persons'    
        ordering=['firstname']
        index_together =(('person_id','firstname'),)

class Movie(models.Model):
    genre_options =(
        ('Horror','Horror'),
        ('Drama','Drama'),
        ('Comedy','Comedy'),
        ('SciFi','SciFi'),
        ('Action','Action'),
        ('Period','Period'),
    )        
    movie_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=180)
    sipnosis=models.TextField(blank=True,null=True)
    Release_Year=models.IntegerField()
    language=models.CharField(max_length=20)
    genre=models.CharField(max_length=20,choices= genre_options)
    top = models.CharField(max_length=180,blank=True,null=True)
    Actor_Actress=models.ManyToManyField(Person,related_name='actor_actress')
    Director=models.ManyToManyField(Person,related_name='director')
    Producer=models.ManyToManyField(Person,related_name='producer')
    state=models.BooleanField(default=True)
    created_at=models.DateTimeField('created_at',auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title





