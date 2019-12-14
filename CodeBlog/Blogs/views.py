from django.shortcuts import render, HttpResponse


# Create your views here.
def blogpost(request, slag):
    return HttpResponse("hello i am in blogposts" + slag)


def bloghome(request):
    return HttpResponse("hello i am in BLOG HOME")
