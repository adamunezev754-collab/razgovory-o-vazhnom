from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Lesson, SiteSettings, Document, ClassCover

def home(request):
    settings = SiteSettings.objects.first()
    documents = Document.objects.all()
    
    covers_list = [
        {'code': '1-2', 'name': '1-2 классы', 'default_img': 'https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&q=80&w=400'},
        {'code': '3-4', 'name': '3-4 классы', 'default_img': 'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&q=80&w=400'},
        {'code': '5', 'name': '5 класс', 'default_img': 'https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&q=80&w=400'},
        {'code': '6-7', 'name': '6-7 классы', 'default_img': 'https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&q=80&w=400'},
        {'code': '8-9', 'name': '8-9 классы', 'default_img': 'https://images.unsplash.com/photo-1554475901-4538ddfbccc2?auto=format&fit=crop&q=80&w=400'},
        {'code': '10-11', 'name': '10-11 классы', 'default_img': 'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&q=80&w=400'},
    ]
    
    for item in covers_list:
        cover = ClassCover.objects.filter(class_name=item['code']).first()
        if cover and cover.image:
            item['image_url'] = cover.image.url
        else:
            item['image_url'] = item['default_img']

    return render(request, 'lessons/home.html', {
        'settings': settings,
        'documents': documents,
        'covers': covers_list
    })

def class_lessons(request, class_name):
    lessons = Lesson.objects.filter(
        Q(target_audience=class_name) | Q(for_all_classes=True),
        is_published=True
    ).distinct()
    
    settings = SiteSettings.objects.first()
    class_display = dict(Lesson.CLASS_CHOICES).get(class_name, class_name)
    
    return render(request, 'lessons/class_lessons.html', {
        'lessons': lessons,
        'class_name': class_name,
        'class_display': class_display,
        'settings': settings
    })

def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk, is_published=True)
    settings = SiteSettings.objects.first()
    return render(request, 'lessons/lesson_detail.html', {'lesson': lesson, 'settings': settings})

def documents_list(request):
    documents = Document.objects.all()
    settings = SiteSettings.objects.first()
    return render(request, 'lessons/documents.html', {'documents': documents, 'settings': settings})