from django.shortcuts import redirect

class BlockLoggedInMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        login_signup_paths = ['/login/', '/signup/']
        if request.user.is_authenticated and request.path in login_signup_paths:
            return redirect('home')
        return self.get_response(request)
