from django.shortcuts import render


# Create your views here.
def three_view(request):
    return render(request, 'three_test.html')
