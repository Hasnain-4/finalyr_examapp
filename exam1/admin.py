from django.contrib import admin

from exam1.models import Contact,Imagepost,Videopost, Userprofile

# Register your models here.
admin.site.register(Contact)
admin.site.register(Imagepost)
admin.site.register(Videopost)
admin.site.register(Userprofile)