from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework.response import Response
import json
from rest_framework.views import APIView
from django.http import HttpResponse, Http404
from eventManagement.responses import *

# Create your views here.
class CreateTicket(APIView):
	# permissions_classes = (permissions.AllowAny, )

	@csrf_exempt
	def post(self, request):
		data = {}
		for key in request.POST.keys():
			data.update(json.loads(key))

		response = init_response()
		email_id = data.get('email_id')
		admin_user = User.objects.filter(email_id=email_id, has_role=True)
		if admin_user:
			price = data.get('price')
			ticket_ins = Ticket(price=price)
			ticket_ins.save()

			return Response({'success': 'User created successfully'})
		else:
			response['status']  = "Action can not be perfomed"
	
class DeleteTicket(APIView):
	# permissions_classes = (permissions.AllowAny, )

	@csrf_exempt
	def post(self, request):
		data = {}
		for key in request.POST.keys():
			data.update(json.loads(key))

		ticket_id = data.get('ticket_id', '')
		response = init_response()
		email_id = data.get('email_id')
		user = User.objects.filter(email_id=email_id)
		if user:
			try:
				Ticket.objects.filter(ticket_id=ticket_id)
			except Ticket.DoesNotExist:
				raise Http404("The requested ticket does not exist.") 
		
			ticket = Ticket.objects.filter(ticket_id=ticket_id).first()
			ticket.delete()
		
			return Response({'success': 'Ticket deleted successfully'})
		else:
			response['status']  = "Action can not be perfomed"

class BookTicket(APIView):

	@csrf_exempt
	def get(self, request):
		data = {}
		for key in request.POST.keys():
			data.update(json.loads(key))
		
		response = init_response()
		user_email_id = data.get('user_email_id')
		admin_email_id = data.get('admin_email_id') 
		event_id = data.get('event_id')
		tic = Ticket.objects.filter(event=event_id).first()
		user = User.objects.filter(email_id=user_email_id, has_role=False)
		admin = User.objects.filter(email_id=admin_email_id)
		if admin:
			user.tickets = tic
			user.save()
			response['ticket_price'] = tic.price
			tic.delete()
			return Response({'success': 'Ticket booked successfully' + response})
		else:
			return Response({'status': 'Ticket can be booked by admin only'})
