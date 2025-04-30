from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Musician, Band, Venue, Room

def musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    return render(request, 'musician.xhtml', {'musician': musician})

def musicians(request):
    all_musicians = Musician.objects.all().order_by('last_name')
    paginator = Paginator(all_musicians, 2) # Show 10 musicians per page
    page_number = request.GET.get('page', 1)
    page_number = int(page_number)

    if page_number > paginator.num_pages:
        page_number = paginator.num_pages
    elif page_number < 1:
        page_number = 1

    page = paginator.page(page_number)
    data = {
        'musicians': page.object_list,
        'page': page,
    }

    return render(request, 'musicians.xhtml', data)

    # Room list view
def room_list(request):
    rooms = Room.objects.select_related('venue').all()
    return render(request, 'rooms.xhtml', {'rooms': rooms})

# Single venue view
def venue_detail(request, venue_id):
    venue = get_object_or_404(Venue.objects.prefetch_related('room_set'), id=venue_id)
    return render(request, 'venue.xhtml', {'venue': venue})