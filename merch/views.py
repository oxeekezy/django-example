from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Чеглок Мерч",
        "name": "Cheglock Sokol Creation",
        "merch": [
            {
                "image": "",
                "name": 'Свитшот "База"',
                "description": "Базовый белый свитшот с логотипом Чеглок база",
                "price": "10.500",
                "sale": 0,
                "count": 10,
            },
            {
                "image": "",
                "name": 'Штаны карго "Техно"',
                "description": "Черные карго штаны из рипстопа с нашивкой Techno Drum",
                "price": "5.990",
                "sale": 0,
                "count": 20,
            },
            {
                "image": "",
                "name": 'Сумка для винила "Vinyl in me"',
                "description": "Шоппер для переноски винила",
                "price": "1.990",
                "sale": 0,
                "count": 99,
            },
            {
                "image": "",
                "name": "Стерео кабель Jack 6.3",
                "description": "Стереокабель Jack 6.3 - Jack 6.3 для подключения акустики с логотипом Cheglock Music",
                "price": "1.500",
                "sale": 999,
                "count": 99,
            },
            {
                "image": "",
                "name": 'Виниловая пластинка "Cheglock Techno Mix pt.1"',
                "description": "Микс с техно вечеринки Cheglock Summer Party в Калининграде",
                "price": "290.000",
                "sale": 0,
                "count": 1,
            },
            {
                "image": "",
                "name": "Фляга с логотипом Cheglock из стали",
                "description": "Железная фляга с логотипом и автогрофом oxeek и dendo.",
                "price": "6.500",
                "sale": 0,
                "count": 15,
            },
        ],
    }

    return render(request, "merch/catalog.html", context)


def product(request):
    return render(request, "merch/product.html")
