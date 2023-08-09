from django.contrib import admin
from .models import Portifolio_detail,Portifolio_section, Contact

# Register your models here.

admin.site.register(Portifolio_detail)

admin.site.register(Portifolio_section)
admin.site.register(Contact)

admin.site.site_header ="Fastwebtech Administration"
admin.site.site_title ="Fastwebtech Administration"
admin.site.index_title ="Welcome to Fastwebtech"
