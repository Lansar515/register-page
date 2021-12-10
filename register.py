def Register(request):
    if request.method == 'POST':
        name=request.POST.get('name')  
        email=request.POST.get('email')  
        mobile_number=request.POST.get('mobile_number')  
        password=request.POST.get('password')  
        confirm_password=request.POST.get('confirm_password')  
        age=request.POST.get('age')  
        gender=request.POST.get('gender')  
        print(name,email,mobile_number,password,confirm_password,age,gender)
      
    return render(request,'register.html')