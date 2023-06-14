from django.shortcuts import render,redirect
from .forms import ContactForm
from articles.models import Article,Author,Category
from contacts.models import Contact

# index page view
def index_view(request):

    # db queries
    articles = Article.objects.all().order_by('-date')[:4]

    # contact form validation
    if request.method == 'POST':
        form =ContactForm(request.POST)

        if form.is_valid():
            
            # getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            # saving the contacts
            contact = Contact(name=m_name,email=email_address,message=mail_message)
            contact.save()
            return redirect('/')
    else:
        form = ContactForm()
    
    context = {
        'articles':articles,
        'form':form,
    }

    # rendering view,
    return render(request,'index.html',context)

