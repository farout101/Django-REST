from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    
    body = request.body
    
    return JsonResponse({'message': 'Welcome to the CFE Home API'})