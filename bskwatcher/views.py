from django.shortcuts import render
import service
from constants import beanstalkd_description, beanstalkd_enabled


# Create your views here.


def index(request):
	stats = service.server_stat()
	display_stats = []
	for k, v in stats.items():
		if k in beanstalkd_enabled:
			display_stats.append(
				{
					'key': k,
					'value': v,
					'display': beanstalkd_description[k]
				})
	return render(request, "bskwatcher/index.html", {'stats': display_stats})


def tube_display(request, t):
	print t
	return render(request, "bskwatcher/tube.html", {})

