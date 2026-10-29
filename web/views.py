from django.shortcuts import render


def inicio(request):
    tarjetas = [
        {
            'titulo': 'Desarrollo web',
            'descripcion': 'Creamos soluciones digitales modernas y funcionales.',
            'icono': '💻',
        },
        {
            'titulo': 'Diseño responsivo',
            'descripcion': 'Adaptamos las páginas a celulares, tabletas y computadores.',
            'icono': '📱',
        },
        {
            'titulo': 'Gestión de datos',
            'descripcion': 'Organizamos la información de forma clara y eficiente.',
            'icono': '🗂️',
        },
    ]

    contexto = {
        'titulo': 'Mi página web',
        'subtitulo': 'Tecnología, diseño e innovación',
        'tarjetas': tarjetas,
    }

    return render(request, 'web/index.html', contexto)