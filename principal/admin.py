from django.contrib import admin
from .models import Autor, Publicacion,Categoria
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	pass



class EntradasLine(admin.TabularInline):
	model = Publicacion

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
	list_display=('nombre','edad','fechanacimiento',)
	list_display_links = ('nombre',)
	search_fields=('nombre',)
	ordering = ('edad',)
	list_filter = ('nombre',)
	inlines = [EntradasLine,]



@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
	list_display = ('autor','titulo','contenido','publicado',)
	list_display_links = ('autor','titulo',)
	search_fields = ('autor__nombre','titulo',)
	ordering = ('autor',)
	list_filter = ('autor','titulo',)
	filter_horizontal =('categoria',)
	actions = ['cambiar_apublicado']

	def cambiar_apublicado(self,request,queryset):
		return queryset.update(publicado=True)
		cambiar_apublicado.short_desciption ='Cambiar a publicado'
	
