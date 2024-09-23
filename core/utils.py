import time

from django.views import View
from django.http import HttpRequest

def function_timer(func):
    # simple decorator for timing functions if you happen to need to benchmark some function
    def decorated_function(*args, **kwargs):
        initial_time = time.time()
        result = func(*args, **kwargs)
        print(f"Elapsed time: {time.time() - initial_time} seconds\n")
        return result
    return decorated_function


def view_timer(view_func: View):
    """
    This is a simple decorator for measuring the server's response time.  
    imo, you'd prolly wanna add your Prometheus stuff inside decorated_view here to keep track of your
    requests in flight, server response timings, etc.

    Also, please note that my decorated_view reads the arguments view and request in that order.
    That's because when I'm declaring the methods for the view, I'll always be using (self, request)
    as args, in that order.
    """

    def decorated_view(view: View, request: HttpRequest, *args, **kwargs):
        
        initial_time = time.time()
        result = view_func(view, request, *args, **kwargs)
        final_time = time.time()
        print("---VIEW TIMER---", f"Endpoint: {request.path}", f"Method: {request.method}", f"Elapsed time: {final_time - initial_time} seconds", sep="\n")
        return result

    return decorated_view
