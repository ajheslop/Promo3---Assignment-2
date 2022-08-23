from telnetlib import STATUS
from unicodedata import name
from django.db import models
from users.models import Profile



# Create your models here.
# django4 supports multiple db's

class Workflow(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True, max_length=30)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    retired = models.BooleanField(default=False)
    # Foreign Keys
    owner = models.ManyToManyField(Profile, blank=True)
    status = models.ForeignKey('Status',on_delete=models.CASCADE)
    steps = models.ManyToManyField('Steps', blank=True)

    
    # status = models.ForeignKey('Status', blank=True,  on_delete=models.CASCADE)
    # tags = models.ManyToManyField('Tag', blank=True, related_name='workflows') 
    # created_by = 
    # requester_id
        
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url
    
        #foreign key 1 to many relationship
class Review(models.Model):
    #owner = 
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return f'workflow: {self.workflow} {self.created}'
    
    
    
    
#many to many relationship with Workflow
class Tag(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return self.name

#many to many relationship with Workflow
class Status(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
    
    
class Steps(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True, max_length=30)
    tags = models.ManyToManyField('Tag', blank=True)
    # status = models.ForeignKey('Status',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    retired = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
       
       
    def __str__(self):
        return self.name

    
    # status = models.ForeignKey('Status', blank=True,  on_delete=models.CASCADE)
    # tags = models.ManyToManyField('Tag', blank=True, related_name='workflows') 
    # created_by = 
    # requester_id
        
 
    
    
#many to many relationship
# Tag to be easily identifiable.
# class Tag(models.Model):
#     name = models.CharField('Workflow', max_length=200, null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     id = models.AutoField(primary_key=True, editable=False)
    
#     def __str__(self):
#         return self.name
    
#    #i want the status/states to be selectable 
# class Status(models.Model):
#     name = models.CharField(Workflow,max_length=200)
#     created = models.DateTimeField(auto_now_add=True)
#     id = models.AutoField(primary_key=True, editable=False)
    


    
#     def __str__(self):
#         return self.name
    
  