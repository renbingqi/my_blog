from django.contrib import admin

# Register your models here.
from classifications.models import Classifications
# Register your models here.
#注册Article 到admin中

admin.site.register(Classifications)