from django.contrib import admin
from .models import Approach,Tool,Scale_Choice,Dicotomic_Choice,Scale_Question,Dicotomic_Question

admin.site.register(Approach)
admin.site.register(Tool)
admin.site.register(Scale_Choice)
admin.site.register(Dicotomic_Choice)
admin.site.register(Scale_Question)
admin.site.register(Dicotomic_Question)
