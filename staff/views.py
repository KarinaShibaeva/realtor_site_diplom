from django.shortcuts import render
from comment.forms import CommentForm
from comment.models import Comment
from staff.models import Staff

def staff_view(request):
    staff_list = Staff.objects.all()
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

    context = {"page": "staff", 'form':form, "staff_list":staff_list}
    return render(request, 'staff/contacts.html', context)
