from django.http import HttpResponse
import models


def index(request, album_id=None):
    all_albums = models.Album.objects.all()
    html = ''

    for album in all_albums:
        url = '/music/' + str(album_id) + '/'
        html += '<a href"' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)

def detail(requst, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")

