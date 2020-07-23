from django.contrib import admin

# Register your models here.
from .models import regis
from .models import ques
admin.site.register(regis)
admin.site.register(ques)