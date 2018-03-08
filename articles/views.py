from articles.models import Article
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    objects = Article.objects.all()
    for obj in objects:
        obj.tran_ch_to_en()
        if len(obj.content) < 5000:
            obj.tran_en_to_ch()
    return render(request, 'Index.html', {'articles': objects})


def detail(request, id):
    try:
        article = Article.objects.get(id=id)
    except:
        return HttpResponse("Sorry to info you the article doesn't exist")

    return render(request, 'detail.html', {'article': article})

