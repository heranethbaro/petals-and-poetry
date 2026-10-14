from django.shortcuts import render


def home(request):
    return render(request, 'flower_shop/home.html')


def about(request):
    return render(request, 'flower_shop/about.html')


def servicesandproducts(request):
    return render(request, 'flower_shop/servicesandproducts.html')


def gallery(request):
    tiles = [
        ('t1', 'Blush bouquet',   'blushbouquet.jpg'),
        ('t2', 'Sunflower table', 'sunflower.jpg'),
        ('t3', 'Greenery wall',   'greenery.jpg'),
        ('t4', 'Lavender bunch',  'lavender.jpg'),
        ('t5', 'Workshop day',    'workshop.jpg'),
        ('t6', 'Library corner',  'library.jpg'),
        ('t7', 'Wedding roses',   'weddingrose.jpg'),
        ('t8', 'Dried flowers',   'driedflowers.jpg'),
    ]
    return render(request, 'flower_shop/gallery.html', {'tiles': tiles})


def contact(request):
    return render(request, 'flower_shop/contact.html')