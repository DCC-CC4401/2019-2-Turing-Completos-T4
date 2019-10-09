from django.contrib import admin

from turing.models import UserProfile, Amigos, Actividades, CreacionActividad

# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Amigos)
admin.site.register(Actividades)
admin.site.register(CreacionActividad)
