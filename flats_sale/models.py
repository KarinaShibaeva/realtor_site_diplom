from django.db import models


class Object(models.Model):
    name=models.CharField(max_length=128, verbose_name="Название")
    text=models.TextField(blank=False, verbose_name="Описание")
    location=models.CharField(max_length=128, verbose_name="Расположение")
    
    class Meta:
       verbose_name = 'Объект'
       verbose_name_plural = 'Объекты'

    def __str__(self):
       return self.name

class Floor(models.Model):
    number = models.IntegerField()

class Category(models.Model):
    name=models.CharField(max_length=128, verbose_name="Название")
    object_name=models.ForeignKey(Object, on_delete=models.CASCADE, verbose_name="Объект")
    price=models.PositiveIntegerField(verbose_name="Цена")
    img=models.ImageField(upload_to="%Y/%m/%d/", verbose_name="Изображение")
    floors = models.ManyToManyField(Floor)

    class Meta:
       verbose_name = 'Категория'
       verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name} - {self.object_name}'

    
class Flat(models.Model):
    object_name=models.ForeignKey(Object, on_delete=models.CASCADE, verbose_name="Объект")
    price=models.PositiveIntegerField(verbose_name='Цена')
    text=models.TextField(blank=False, verbose_name="Описание")
    img=models.ImageField(upload_to="%Y/%m/%d/", verbose_name="Изображение")
    
    class Meta:
       verbose_name = 'Объявление'
       verbose_name_plural = 'Объявления'

    def __unicode__(self):
        return self.object_name.name

class Contract(models.Model):
    number = models.CharField(max_length=128, verbose_name='Номер договора')
    object = models.ForeignKey(Object, on_delete=models.CASCADE, verbose_name='Название объекта')

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'

