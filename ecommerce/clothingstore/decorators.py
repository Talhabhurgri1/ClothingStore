from django.shortcuts import redirect

#a decorator for un_authorized users
def unauthenticated_user(view_func):
    def wrapper(request,*args,**kwargs):
        print(f'User Active: {request.user}')
        print(f'User : {request.user.is_authenticated}')

        if request.user.is_authenticated:
            
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)

    return wrapper



