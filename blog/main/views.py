from django.shortcuts import render

def main(request):
    '''
    Render the main page
    '''
    context = {'like':'Django is excellent '}
    return render(request, 'main/main.html', context)

def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')