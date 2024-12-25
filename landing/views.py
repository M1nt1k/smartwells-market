from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from market_django import settings
from academy.models import Item
from academy.paginator import paginator

def index(request):
    carousel_items = [
        {
            'title': 'Инновационные решения для бурения скважин',
            'description': 'Используйте нашу систему мониторинга, которая автоматизирует процессы бурения и улучшает контроль на каждом этапе.',
            'image_url': '/static/assets/images/main/carousel/sea-platform.jpg',
        },
        {
            'title': 'Современные навыки для специалистов нефтегазовой отрасли',
            'description': 'Обучение для инженеров и специалистов отрасли. Развивайте профессиональные навыки с использованием актуальных технологий.',
            'image_url': '/static/assets/images/main/carousel/logic-controller.jpg',
        },
        {
            'title': 'Поддержка на каждом этапе',
            'description': 'Получите экспертные консультации и техническую поддержку для внедрения решений и обучения вашей команды.',
            'image_url': '/static/assets/images/main/carousel/talking-about-business.jpg',
        },
    ]

    advantages_items = [
        {
            'title': 'Актуальные знания от экспертов',
            'text': 'Наши курсы разрабатываются практикующими профессионалами в сфере бурения и нефтегазовой индустрии.',
        },
        {
            'title': 'Передовое программное обеспечение',
            'text': 'Инструменты, которые упрощают проектирование скважин, прогнозирование аварий и управление процессами.',
        },
        {
            'title': 'Поддержка 24/7',
            'text': 'Техническая помощь и консультации для ваших специалистов в любое время.',
        },
        {
            'title': 'Экономия времени и ресурсов',
            'text': 'Повышение эффективности процессов за счет внедрения современных технологий.',
        },
        {
            'title': 'Надежность и доверие',
            'text': 'Мы сотрудничаем с лидерами отрасли и гарантируем высокое качество всех наших услуг.',
        }
    ]

    items = Item.objects.filter(is_available=True)[:3]

    carousel_demo = [
        {
            'title': 'Realtime-Screen',
            'image_url': 'static/assets/images/main/program/carousel/Realtime.png'
        },
        {
            'title': 'RetroTime-Screen',
            'image_url': 'static/assets/images/main/program/carousel/RetroTime.png'
        },
        {
            'title': 'RetroDepth-Screen',
            'image_url': 'static/assets/images/main/program/carousel/RetroDepth.png'
        },
        {
            'title': 'Balance-Screen',
            'image_url': 'static/assets/images/main/program/carousel/Balance.png'
        },
        {
            'title': 'Inclinometry-Screen',
            'image_url': 'static/assets/images/main/program/carousel/Inclinometry.png'
        },
    ]

    program_items = [
        {
            'title': 'Снижение затрат',
            'text': 'уменьшение времени на планирование и бурение.'
        },
        {
            'title': 'Повышение точности',
            'text': 'современные алгоритмы и прогнозирование.'
        },
        {
            'title': 'Поддержка 24/7',
            'text': 'оперативная помощь в любой ситуации.'
        },
    ]

    if request.method == 'POST':
        
        form = ContactForm(request.POST)

        if form.is_valid():
            email_subject = 'SMARTWELLS.RU :: Сообщение через контактную форму '
            email_body = "С сайта отправлено новое сообщение\n\n" \
                         "Имя отправителя: %s \n" \
                         "E-mail отправителя: %s \n\n" \
                         "Сообщение: \n" \
                         "%s " % \
                         (form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            try:
                send_mail(
                    email_subject, email_body,
                    settings.EMAIL_HOST_USER, ['target_email@example.com'],
                    fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("landing:index")

    form = ContactForm()

    return render(request, 'landing/index.html', {
        'carousel_items': carousel_items,
        'advantages_items': advantages_items,
        'page_obj': items,
        'carousel_demo': carousel_demo,
        'program_items': program_items,
        'form': form,
    })


def about(request):
    company_info_params = [
        {
            'param': 'Наименование:',
            'info': 'ООО "НПП ИНТЭК-ИНЖИНИРИНГ"'
        },
        {
            'param': 'ИНН:',
            'info': '7203391384'
        },
        {
            'param': 'КПП:',
            'info': '720301001'
        },
        {
            'param': 'ОГРН:',
            'info': '1167232076890'
        },
        {
            'param': 'Расч. счёт:',
            'info': ''
        },
        {
            'param': 'Корр. счёт:',
            'info': ''
        },
        {
            'param': 'БИК:',
            'info': ''
        },
        {
            'param': 'Телефон:',
            'info': '+7 (3452) 393-349'
        },
        {
            'param': 'Юридический адрес:',
            'info': '625014, Тюменская область, город Тюмень, ул. Чекистов, д. 38, офис 7'
        },
    ]

    return render(request, 'landing/about.html', {
        'company_info_params': company_info_params
    })

def contract_offer(request):
    return render(request, 'landing/contract_offer.html')

def privacy(request):
    return render(request, 'landing/privacy.html')

def products(request):
    return render(request, 'landing/template.html')
