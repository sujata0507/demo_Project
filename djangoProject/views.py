from django.http import HttpResponse
# #from django.shortcuts import render

# def homepage(request):
#     return HttpResponse('homepage')
#     #return render(request,'homepage.html')

# def about(request):
#     return HttpResponse('about')
#     #return render(request,'About.html')



def home_page(request):
    print('home page requested')
    return HttpResponse("This is homepage")