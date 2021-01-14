from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    return render(request,'index.html',{})
def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            message_name,
            message,
            message_email,
            ['kaunghtetsan6574@gmail.com']

        )
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})
def about(request):
    return render(request,'about.html',{})
def services(request):
    return render(request,'service.html',{})
def blog1(request):
    return render(request,'blog.html',{})
def blog2(request):
    return render(request,'blog-details.html',{})
def pricing(request):
    return render(request,'pricing.html',{})


