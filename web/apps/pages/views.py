from django.shortcuts import render

def home_view(request):
    """
    Основная страница приложения (Landing Page).
    """
    return render(request, 'pages/home.html', {
        'title': 'Welcome to Nomondays',
        'content': 'Your journey starts here.'
    })
