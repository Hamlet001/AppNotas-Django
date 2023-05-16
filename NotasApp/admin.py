from django.contrib import admin
from .models import Nota

class NotaAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha", )

# Register your models here.
admin.site.register(Nota, NotaAdmin)