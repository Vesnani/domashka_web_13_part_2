
from django.contrib import admin
from quoteapp.models import Tag, Author, Quote, MyModel

# Register your models here.
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Quote)
admin.site.register(MyModel)
