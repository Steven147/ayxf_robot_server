from django.http import HttpResponse, HttpRequest, JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    return HttpResponse("hello, linshaoqin")


@csrf_exempt # close csrf check
def card(request: HttpRequest):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        challenge_value = received_json_data['challenge']
        return JsonResponse({'challenge': challenge_value})
