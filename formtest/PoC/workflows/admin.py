from django.contrib import admin

# Register your models here.
from . models import Workflow, Review, Tag, Status, Steps

admin.site.register(Workflow)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Status)
admin.site.register(Steps)

