from django.core.paginator import Paginator
from django.shortcuts import render
from App import models

from utils.pager import PageInfo


def index(request):
    current_page = request.GET.get('page')

    user_list = models.UserInfo.objects.all()

    paginator = Paginator(user_list, 10)
    pg = paginator.page(current_page)

    return render(request, 'index.html', {'pg': pg})


def custom(request):
    all_count = models.UserInfo.objects.count()

    page_info = PageInfo(request.GET.get('page'), all_count, 10, show_page=5)
    user_list = models.UserInfo.objects.all()[page_info.start():page_info.stop()]

    return render(request, 'custom.html', {'user_list': user_list, 'page_info': page_info})