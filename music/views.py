from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is Music</h1>")

def detail(requst, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")

