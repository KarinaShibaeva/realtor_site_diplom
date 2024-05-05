from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    
    class Meta:
       verbose_name = 'Должность'
       verbose_name_plural = 'Должности'

    def __str__(self):
       return self.name

class Staff(models.Model):
    first_name = models.CharField(max_length=128, verbose_name="Фамилия")
    name = models.CharField(max_length=128, verbose_name="Имя")
    last_name = models.CharField(max_length=128, verbose_name="Отчество")
    post_name = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Должность")
    img = models.ImageField(upload_to="%Y/%m/%d/", verbose_name="Фотография")

    class Meta:
       verbose_name = 'Сотрудник'
       verbose_name_plural = 'Сотрудники'
