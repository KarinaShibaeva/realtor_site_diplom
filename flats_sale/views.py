from django.shortcuts import render, get_object_or_404
from flats_sale.models import Flat, Category, Object, Floor
from django.views.generic import ListView
from flats_sale.forms import FlatSearchForm
from comment.forms import CommentForm
from comment.models import Comment
from django.core.paginator import Paginator
from django.contrib import messages

class SaleListView(ListView):
    model = Flat
    context_object_name = 'flats_sale'
    template_name = 'flats_sale/flats_sale.html'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['object-count'] = self.model.objects.count()
        paginator = Paginator(self.model.object_list, self.paginate_by)
        try:
            page = self.request.GET.get('page')
        except:
            page = 1
           
        try:
            context[self.context_object_name] = paginator.page(page)
        except:
            context[self.context_object_name] = paginator.page(1)
           
        context['object-count'] = self.model.objects.count()
        context['paginator'] = paginator
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = FlatSearchForm()         
        return context                          

    def get(self, request, *args, **kwargs):

        form = FlatSearchForm(self.request.GET)
        if form.is_valid():
           cd = form.cleaned_data
           flats = self.model.objects.filter(object_name__name__iexact=cd['search'])
        else:
            flats = self.model.objects.all()

        return render(request, self.template_name, self.get_context_data(object_list=flats))
    

def sale_id_view(request, pk):
    object_list = Object.objects.filter(pk=pk)

    # Получаем список категорий, связанных с этим объектом
    category_list = Category.objects.filter(object_name=pk)


    #comments = pk.comments.all()
    pk = get_object_or_404(Flat, pk=pk)
    if request.method=="POST": 
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid(): 
            obj = Comment() #gets new object
            obj.author = form.cleaned_data['author']
            obj.email = form.cleaned_data['email']
            obj.phone = form.cleaned_data['phone']
            obj.text = form.cleaned_data['text']
            #finally save the object in db
            obj.save()
            messages.success(request, 'Ваша заявка отправлена')
            form = CommentForm()

    else:
        form = CommentForm()

    context = {"pk": pk, 'page': 'flats',  # 'comments_list':comments,
               'form': form, 'category_list': category_list,
               'object_list': object_list}
    return render(request, "flats_sale/flats_detail.html", context)