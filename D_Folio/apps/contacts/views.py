from django.shortcuts import render

from .models import Project_request, Project_ask_request, Website_error_request, Other_request

# Create your views here.

def index(request):
	return render(request, 'contacts/main.html')

def request(request):
	user_subject = request.POST['subject']

	user_name = request.POST['name']
	user_email = request.POST['email']

	user_text = request.POST['message']

	if user_subject == '1':
		obj = Project_request(sender_name = user_name, sender_email = user_email, sender_text = user_text)
	elif user_subject == '2':
		obj = Project_ask_request(sender_name = user_name, sender_email = user_email, sender_text = user_text)
	elif user_subject == '3':
		obj = Website_error_request(sender_name = user_name, sender_email = user_email, sender_text = user_text)
	elif user_subject == '4':
		obj = Other_request(sender_name = user_name, sender_email = user_email, sender_text = user_text)

	obj.save()

	return render(request, 'contacts/sended.html')
