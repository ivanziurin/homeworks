from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))

# find qty of pages in csv
id = []
with open('data-398-2018-08-30.csv') as csvfile:
    total_page = 0
    file = csv.DictReader(csvfile)
    for raw in file:
        id.append(raw['ID'])

# separated by 10 pc list of id numbers
sep = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
sep_id = sep(id, 10)


def bus_stations(request):

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(id, 10)
    page = paginator.get_page(page_number)

    chosen_ind = sep_id[page_number-1] # find the list of id should be chosen for pagination
    with open('data-398-2018-08-30.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row for row in reader if row['ID'] in chosen_ind]  # find the list of rows for pagination

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
         'bus_stations': rows,
         'page': page,
    }
    return render(request, 'stations/index.html', context)