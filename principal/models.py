from django.db import models

class Autor(models.Model):
	nombre = models.CharField(max_length=120)
	edad = models.IntegerField(max_length=50)
	fechanacimiento = models.DateField(null=True)

	def __unicode__(self):
		return self.nombre 


class Categoria(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre


class Publicacion(models.Model):
	autor = models.ForeignKey(Autor)
	titulo = models.CharField(max_length=150)
	categoria = models.ManyToManyField(Categoria)
	contenido = models.TextField()
	publicado = models.BooleanField(default=False)

	def __unicode__(self):
		return "%s %s" % (self.autor,self.titulo)

 