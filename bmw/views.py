from django.shortcuts import render_to_response, redirect
from models import Center
from django.template import RequestContext
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.signals import post_save

def home(request):
	return render_to_response('home.html', context_instance=RequestContext(request))

@login_required
def man_home(request):
	
	cnt = User.objects.count()
	woman_list=[]
	for i in range(1, cnt+1):
		user = User.objects.get(pk=i)
		if user.get_profile().sex==0:
			woman_list.append(user)

	return render_to_response('man_home.html', {'woman_list':woman_list}, context_instance=RequestContext(request))

@login_required
def woman_home(request):
	cnt = User.objects.count()
	man_list=[]
	for i in range(1, cnt+1):
		user = User.objects.get(pk=i)
		if user.get_profile().sex==1:
			man_list.append(user)
	return render_to_response('woman_home.html', {'man_list':man_list}, context_instance=RequestContext(request))

def login(request):
	user_id = request.POST['user_id']
	password = request.POST['password']
	user = authenticate(username=user_id, password=password)
	if user is not None:
		if user.is_active:
			auth_login(request, user)  #login succeeded
			#return redirect('/man_home')   #for men
			
			if user.get_profile().sex==1:
				return redirect('/man_home')   #for men
			else:
				return redirect('/woman_home') #for women
			
		else:
			return redirect('/home')
	else:
		return redirect('/admin') #can't use Man's function

@login_required
def logout_view(request):
    logout(request)
    return redirect('/home')

def create_user(request):
	user_id = request.POST['user_id']
	password = request.POST['password']

	new_user = User.objects.create_user(user_id, None, password)
	new_user.save()

	user = authenticate(username=user_id, password=password)
	if user is not None:
		if user.is_active:
			auth_login(request, user)  #login succeeded

	return redirect('/home')


		
