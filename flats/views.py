from django.shortcuts import render
from comment.forms import CommentForm
from comment.models import Comment
from django.contrib import messages

def flat_list_view(request):
    
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
            form = CommentForm() 
    else:
        form = CommentForm()

    context = {'page':'flats', #'comments_list':comments,
               'form':form}
    return render(request, "flats/flats_list.html", context)

def flat_sell_view(request):
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
            form = CommentForm()
    else:
        form = CommentForm()

    context = {'page':'flats','form':form}
    return render(request, 'flats/flats_sell.html', context)

def flats_sale2_view(request):
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
            form = CommentForm()
    else:
        form = CommentForm()
    context = {"page": "flats_sale2", 'form':form}
    return render(request, 'flats/flats_sale2.html', context)

