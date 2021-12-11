from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'karbonara': {
        'спагетти, гр': 100,
        'сливки, гр': 60,
        'пармезан, гр': 10,
        'бекон, гр': 80,
        'желтки, шт': 1,
    },
    # можете добавить свои рецепты ;)
}

def home_view(request):
    return HttpResponse('Введите название блюда')

def recepies(request, recipe_name):
    dish_counter = int(request.GET.get('servings', 1))
    context = {'recipe': dict(map((lambda x: (x, float(DATA[recipe_name][x])*dish_counter)),
                                  DATA[recipe_name].keys()))}
    return render(request, 'calculator/index.html', context)
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
