from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    category = models.CharField(max_length = 156)
    def __str__(self):
        return self.category

class Tags(models.Model):
    tags = models.CharField(max_length = 156)
    def __str__(self):
        return self.tags    

class Author(models.Model):
    description = RichTextUploadingField()
    name = models.CharField(max_length = 156)
    position = models.CharField(max_length = 156)
    fb =models.CharField(max_length = 156,blank=True, null=True)
    insta = models.CharField(max_length = 156, blank=True, null=True)
    linkedin = models.CharField(max_length = 156, blank=True, null=True)
    image  = models.ImageField(upload_to="SEO")
    def __str__(self):
        return self.name     
               
# Create your models here.
class Blog(models.Model):
    status  = models.BooleanField(default=True)
    
    h1  = models.CharField(max_length = 156)
    slug =models.CharField(max_length = 1256,blank=True, null=True)
    page_name = models.CharField(max_length = 1256,blank=True, null=True)
    keyword = models.CharField(max_length = 156)
    description = models.CharField(max_length = 900)
    title = models.CharField(max_length = 156)
    breadcrumb = models.CharField(max_length = 156)
    canonical = models.CharField(max_length = 900, default="https://straightlinesource.com/")
    og_type =models.CharField(max_length = 156)
    og_card = models.CharField(max_length = 156)
    og_site = models.CharField(max_length = 156)
    image  = models.ImageField(upload_to="SEO")
    
    category = models.ManyToManyField(Category)
    tag  = models.ManyToManyField(Tags)
    updated  = models.DateField(auto_now=True)
    

    blog_banner_lg = models.ImageField(upload_to="Page Data", blank=True, null=True)
    blog_banner_sm = models.ImageField(upload_to="Page Data", blank=True, null=True)
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published  = models.DateField()
    content = RichTextUploadingField()
    active = True
    edits = RichTextUploadingField( blank=True, null=True)
    schema = models.TextField(max_length = 15622, blank=True, null=True)
    guide_image = models.ImageField(upload_to="Page Data", blank=True, null=True)
    guide = RichTextUploadingField( blank=True, null=True)
    def __str__(self):
        return self.h1

   



class Team(models.Model):   
    image  = models.ImageField(upload_to="SEO")
    name = models.CharField(max_length = 156)
    position = models.CharField(max_length = 156)
    fb = models.CharField(max_length = 156)
    insta = models.CharField(max_length = 156)
    twitter = models.CharField(max_length = 156)
    youtube = models.CharField(max_length = 156)

    def __str__(self):
        return self.name
        

class Testimonials(models.Model):   
    image  = models.ImageField(upload_to="SEO")
    name = models.CharField(max_length = 156)
    position = models.CharField(max_length = 156)
    review = models.TextField()
 
    def __str__(self):
        return self.name

class Industry(models.Model):   
    name = models.CharField(max_length = 156)
    info = models.TextField()   
    headline = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
      
    
    
class Careers(models.Model):
    position = models.CharField(max_length = 156)
    location = models.CharField(max_length = 156)
    description = RichTextUploadingField()
    def __str__(self):
        return self.position     
 

class Terms_and_condition(models.Model):
    description = RichTextUploadingField()
    

class Referral_terms_and_condition(models.Model):
    description = RichTextUploadingField()
    

class Privacy_policy(models.Model):
    description = RichTextUploadingField()
    