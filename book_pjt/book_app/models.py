from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Category(models.Model):
    name=models.CharField(max_length=50,null=True)


    def __str__(self):
        return self.name



class Books(models.Model):
    name=models.CharField(max_length=100,null=True)
    author=models.CharField(max_length=50,null=True)
    cover=models.ImageField(upload_to='image',blank=True)
    price=models.IntegerField()
    is_published=models.BooleanField(default=False)
    section=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        verbose_name='books'
        verbose_name_plural='books'

    def __str__(self):
        return self.name
    


class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    content=models.TextField()

    def __str__(self):
        return self.content
    


