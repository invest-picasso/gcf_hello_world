import functions_framework

@functions_framework.http
def handler(request):
    return 'Hello World'