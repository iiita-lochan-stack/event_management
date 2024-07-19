from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework.response import Response
import json
from rest_framework.views import APIView
from django.http import HttpResponse, Http404
from eventManagement.responses import *

# Create your views here.
class AddEvent(APIView):

	@csrf_exempt
	def post(self, request):
		data = {}
		for key in request.POST.keys():
			data.update(json.loads(key))

		admin_email_id = data.get('admin_email_id', '')
		admin = User.objects.filter(email_id=admin_email_id, has_role=True)
		if admin:
			name = data.get('name')
			location = data.get('location')
			start_date = data.get('start_date')
			end_date = data.get('end_date')
			event_ins = Event(name=name, location=location, start_date=start_date, end_date=end_date)
			event_ins.save()

			return Response({'success': 'Event created successfully'})
		else:
			return Response({'Failure': 'Event can be created by admin user only'})

class GetAllEvent(APIView):
	@csrf_exempt
	def get(self, request):
		data = {}
		code = 0
		response = init_response()
		for key in request.POST.keys():
			data.update(json.loads(key))

		email_id = data.get('email_id', '')
		user = User.objects.filter(email_id=email_id)
		if user:
			try:
				events = Event.objects.all()
				for event in events:
					response['event_id'] = event.event_id
					response['name'] = event.name
					response['location'] = event.location
					response['start_date'] = event.start_date
					response['end_date'] = event.end_date
					tickets = event.available_tickets
					ticket_detail = {}
					for tic in tickets:
						ticket_detail['ticket_id'] = tic.ticket_id
						ticket_detail['ticket_price'] = tic.ticket_price
						ticket_detail["created_at"] = tic.created_at
						ticket_detail["updated_at"] = tic.updated_at

					response["ticket"] = ticket_detail
				
				response['status']  = "Event details fetched succesfully"
			except Event.DoesNotExist:
				raise Http404("The requested event does not exist.") 

			return send_201(response) if code == '0' else send_400(response)
		else:
			response['status']  = "Action can not be perfomed"
	

# class GetEvent(APIView):
# 	@csrf_exempt
# 	def get(self, request):
# 		data = {}
# 		for key in request.GET.keys():
# 			data.update(json.loads(key))
		
# 		code = 0
# 		response = init_response()
# 		event_id = data.get('event_id', '')
# 		email_id = data.get('email_id', '')
# 		user = User.objects.filter(email_id=email_id)
# 		if user:
# 			try:
# 				event = Event.objects.get(event_id=event_id)
# 				tickets = event.available_tickets
# 				ticket_detail = {}
# 				for tic in tickets:
# 					ticket_detail['ticket_id'] = tic.ticket_id
# 					ticket_detail['ticket_price'] = tic.ticket_price
# 					ticket_detail["created_at"] = tic.created_at
# 					ticket_detail["updated_at"] = tic.updated_at
				
# 				response['event_id'] = event.event_id
# 				response['name'] = event.name
# 				response['location'] = event.location
# 				response["ticket"] = ticket_detail
# 				response['start_date'] = event.start_date
# 				response['end_date'] = event.end_date
# 				response['status']  = "Event details fetched succesfully"
# 			except Event.DoesNotExist:
# 				raise Http404("The requested event does not exist.") 

# 			return send_201(response) if code == '0' else send_400(response)
# 		else:
# 			response['status']  = "Action can not be perfomed"
	
	
class GetEvent(APIView):
	@csrf_exempt
	def post(self, request):
		data = {}
		for key in request.POST.keys():
			data.update(json.loads(key))
		
		email_id = data.get('email_id', '')
		user = User.objects.filter(email_id=email_id)
		if user:
			code = 0
			response = init_response()
			event_id = data.get('event_id', '')
			nu_of_tickets = data.get('nu_of_tickets', '')
			
			try:
				event = Event.objects.get(event_id=event_id)
				for ticket in nu_of_tickets:
					tic = Ticket(price=20)
					event.available_tickets = tic
					event.save()

				response['status']  = "Ti ket for an event  created succesfully"
			except Event.DoesNotExist:
				raise Http404("The requested event does not exist.") 

			return send_201(response) if code == '0' else send_400(response)
		else:
			response['status']  = "Action can not be perfomed"