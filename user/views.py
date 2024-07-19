from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework.response import Response
import json
from rest_framework.views import APIView
from django.http import HttpResponse, Http404

# Create your views here.
class CreateUser(APIView):
	# permissions_classes = (permissions.AllowAny, )

	@csrf_exempt
	def post(self, request):
		data = {}
		for key in request.POST.keys():
			data.update(json.loads(key))
		
		response = init_response()
		email_id = data.get('email_id')
		user = User.objects.filter(email_id=email_id)
		if user:

			first_name = data.get('first_name')
			middle_name = data.get('middle_name')
			last_name = data.get('last_name')
			mobile_number = data.get('mobile', '')
			email = data.get('email', '')
			
			if User.objects.filter(email_id=email).exists():
				return Response({'error': 'Email id already exits'})
			else:
				user_ins = User(first_name=first_name, middle_name=middle_name, last_name=last_name, \
														mobile_number=mobile_number,\
											email_id=email)
				user_ins.save()

			return Response({'success': 'User created successfully'})
		else:
			response['status']  = "Action can not be perfomed"
	
class DeleteUser(APIView):
	# permissions_classes = (permissions.AllowAny, )

	@csrf_exempt
	def post(self, request):
		data = {}
		for key in request.POST.keys():
			data.update(json.loads(key))

		email = data.get('email', '')
		
		try:
			User.objects.filter(email_id=email)
		except User.DoesNotExist:
			raise Http404("The requested user does not exist.") 
	
		user = User.objects.filter(email=email).first()
		user.delete()
	
		return Response({'success': 'User deleted successfully'})