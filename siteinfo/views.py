from django.db.models.functions import datetime
from django.shortcuts import render
from datetime import date

from comment.models import Comment


def main_view(request):
    from datetime import date
    # Дата основания фирмы
    company_founded = date(2004, 1, 1)

    # Получаем текущую дату
    current_date = date.today()

    # Вычисляем разницу в годах между текущей датой и датой основания фирмы
    years_working = current_date.year - company_founded.year
    total_applications = Comment.objects.count()
    context = {"page": "main", "years_working": years_working, "total_applications": total_applications}
    return render(request, 'siteinfo/main.html', context)

def about_view(request):
    context = {"page": "about"}
    return render(request, 'siteinfo/about.html', context)

