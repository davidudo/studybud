from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateRooms(request, rooms, results):

    page = request.GET.get('page')
    paginator = Paginator(rooms, results)

    try:
        rooms = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        rooms = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        rooms = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, rooms

def paginateActivity(request, room_messages, results):

    page = request.GET.get('page')
    paginator = Paginator(room_messages, results)

    try:
        room_messages = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        room_messages = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        room_messages = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, room_messages