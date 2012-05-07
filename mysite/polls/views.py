from django.template import loader, RequestContext
from polls.models import *
#from forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login

def base(request):
    return render_to_response('base.html')

def login(request):
    return render_to_response('login.html')

def home(request):
    return render_to_response('home.html')

def cv(request):
    return render_to_response('cv.html')

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            form.save()
            #cc_myself = form.cleaned_data['cc_myself']
            #recipients = ['info@example.com']
            #if cc_myself:
            #    recipients.append(sender)
            # commented out the email part for now...       
            # from django.core.mail import send_mail
            # send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form
    return render_to_response('contact.html', {'form': form,}, context_instance=RequestContext(request))


def thanks(request):
    return render_to_response('thanks.html')

def safespace(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return render_to_response('safespace.html')
        else:
            # Return a 'disabled account' error message
            print "Your account has been disabled!"
    else:
        # Return an 'invalid login' error message.
        return render_to_response('thanks.html')


def register(request):
    if request.method == 'POST': # If the form has been submitted...
        form = UserForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user
            return render_to_response('thanks.html')
        else:
            print "Your account has been disabled!"    
    else:
        form = ContactForm() # An unbound form
    return render_to_response('register.html', {'form': form,}, context_instance=RequestContext(request))



def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('index.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('detail.html', {'poll': p})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)


 #create a profile without a survey in mind
def create_search_profile(request):
    if request.method == 'POST':
        user_form = UserRegForm(request.POST)
        form = SearchRegForm(request.POST, request.FILES)
        if form.is_valid() and user_form.is_valid():
#upload photo
            file = request.FILES["file"]
            store_in_s3(file)
            p = PhotoUrl(url="http://roommater.s3.amazonaws.com/"+str(file))
            p.save()
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            newprofile = UserProfile(pic=p.url, user=user,
                             name=request.POST['name'],
                             about=request.POST['about'])
            newprofile.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            if request.REQUEST.get('next' '') != None:
                redirect_to = request.REQUEST.get('next' '')
            else: 
                redirect_to = '/dash/'
            return redirect(redirect_to)
    else:
        user_form = UserRegForm()
        form = SearchRegForm()
    return render_to_response('login.html', {'form':form, 'user_form':user_form}, context_instance=RequestContext(request))    


