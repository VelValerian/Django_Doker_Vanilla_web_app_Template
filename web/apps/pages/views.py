from django.shortcuts import render

def home_view(request):
    """
    Основная страница приложения (Landing Page).
    """
    return render(request, 'pages/home.html', {
        'title': 'BrandName | Creative Design Studio',
        'subtitle': 'Премиальные веб-решения для современного бизнеса. Мы создаем цифровой опыт, который вдохновляет.'
    })

def about_view(request):
    """
    Страница "О нас" (About Us).
    """
    return render(request, 'pages/about.html', {
        'title': 'О компании',
        'subtitle': 'Наш путь, наши ценности и наше видение будущего.'
    })

def contacts_view(request):
    """
    Страница контактов (Contacts).
    """
    return render(request, 'pages/contacts.html', {
        'title': 'Свяжитесь с нами',
        'subtitle': 'Мы всегда открыты для новых идей и интересных проектов.'
    })
