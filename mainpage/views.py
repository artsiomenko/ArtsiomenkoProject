from django.shortcuts import render


def index(request):
    news = [
        {
            'description': 'South Korea’s Moon Jae-in sworn in vowing to address North'
        },
        {
            'description': 'No charges over 2017 Conservative battle bus cases'
        },
    ]
    return render(request, 'index.html', {'news': news})
