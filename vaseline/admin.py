from django.contrib import admin

# Register your models here.
from .models import Sett,Question,Answer


admin.site.register(Sett)
admin.site.register(Question)
admin.site.register(Answer)