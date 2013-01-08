from django.shortcuts import render_to_response

def homepage_view(request):
	return render_to_response("temp.html")