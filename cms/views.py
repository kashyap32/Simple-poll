from .forms import UserDetailForm, UserCreateForm, LogInForm
from django.template.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from django.shortcuts import render,get_object_or_404,HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader,RequestContext
from .models import Question,Choice
# Create your views here.

def SignUp(request):
	form = UserCreateForm(request.POST or None)
	form1 = UserDetailForm(request.POST or None)

	if form.is_valid() and form1.is_valid():
		instance = form.save()
		extradetails = form1.save(commit = False)
		extradetails.user = instance
		extradetails.save()
		messages.success(request, "You have successfully registered")
		return HttpResponseRedirect("/")

	context = {
		'form':form,
		'form1':form1
	}
	context.update(csrf(request))

	return render(request, 'signup.html', context)

def LogIn(request):
	form = LogInForm(request.POST or None)

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)

				return HttpResponseRedirect("/home/")

		else:
			messages.error(request, "Incorect Username or Password")

	context = {
		'form':form,
	}

	context.update(csrf(request))
	return render(request, 'login.html', context)

@login_required
def Home(request):
	user = request.user
	phone = UserDetail.objects.filter(user__username = user)
	print phone
	latest_q=Question.objects.order_by('-pub_date')[:5]
          
	context = {
		'phone':phone,
                'latest_q':latest_q
                }

	if request.method == 'POST':
		if request.POST.get('logout') == 'logout':
			logout(request)
			return HttpResponseRedirect("/")

	return render(request, 'home.html', context)



@login_required

def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)

    return render(request,'detail.html',{'question':question})
@login_required

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'results.html',{'question':question})
@login_required

def vote(request,question_id):

    question=  get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request,'detail.html',{'question':question,'error_message':"Please select choice"})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('cms:results',args={question_id,}))







	



