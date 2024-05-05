from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=32, verbose_name="Имя")
    email=models.CharField(max_length=128, verbose_name="Email")
    phone=models.CharField(max_length=32, verbose_name="Телефон")
    text = models.TextField(blank=False, verbose_name="Вопрос")
    date_of_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправления")
    consideration = models.BooleanField(default=False, verbose_name="Рассмотрена")
    
    
    def __str__(self):
        return self.text [ :32] + '...'
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ('-date_of_create', )
        
   