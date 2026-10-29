from django.shortcuts import render

def inicio(request):
    contexto = {
        'titulo': 'Página Principal Django',
        'subtitulo': '¡Entorno Virtual, Git, Vistas y CSS Configurados Exitosamente!',
        'modulos': [
            'Aislamiento de dependencias con venv',
            'Estructura modular con Django',
            'Control de versiones con Git & .gitignore',
            'Renderizado dinámico de plantillas HTML5 + CSS3'
        ]
    }
    return render(request, 'web/index.html', contexto)