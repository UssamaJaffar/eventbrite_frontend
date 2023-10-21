from django.shortcuts import redirect


def authentication_not_required(view_func, redirect_url="/event/"):
    """
        this decorator ensures that a user is not logged in,
        if a user is logged in, the user will get redirected to 
        the url whose view name was passed to the redirect_url parameter
    """
    def wrapper(request, *args, **kwargs):
        if not request.session.get('access_token'):
            return view_func(request,*args, **kwargs)
        return redirect(redirect_url)

    return wrapper


def authentication_required(view_func, redirect_url="/user/login/"):
    """
        this decorator ensures that a user is not logged in,
        if a user is logged in, the user will get redirected to 
        the url whose view name was passed to the redirect_url parameter
    """
    def wrapper(request, *args, **kwargs):
        if request.session.get('access_token'):
            return view_func(request,*args, **kwargs)
        return redirect(redirect_url)

    return wrapper