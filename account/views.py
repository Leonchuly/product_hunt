from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    elif request.method == 'POST':
        user_name = request.POST['用户名']
        password1 = request.POST['密码']
        password2 = request.POST['确认密码']
        try:
            User.objecrs.get(username=user_name)
            return render(request, 'signup.html', {'用户名错误':'该用户名已存在'})
        except User.DoesNotExits:
            if password1 == password2:
                User.objects.create(username=user_name, password=password1)
                return redirect('main')
            else:
                pass