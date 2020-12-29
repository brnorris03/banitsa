from django.http import HttpResponse
from django.shortcuts import render
import random

from .models import Fortune

def reset_context():
    return {'picked': [], 'already_picked_list': [], 'final': False, 'latest': None,
            'count': 0, 'total': Fortune.objects.count(), 'available': list(Fortune.objects.all().values_list('pk', flat=True))}

def index(request):
    if not 'context' in request.session.keys():
        context =reset_context()
        request.session['context'] = context
        request.session.set_expiry(7200)
    else:
        context = request.session['context']
    return render(request, 'banitsa/index.html', context)

def pick(request):
    if request.POST.get('reset'):
        context = reset_context()
        request.session['context'] = context
        return render(request, 'banitsa/index.html', context)

    context = request.session['context']
    if context['final']:
        return render(request, 'banitsa/index.html', context)

    num_fortunes = context['total']
    if len(context['picked']) >= num_fortunes:
        context['final'] = True
        request.session['context'] = context
        return render(request, 'banitsa/index.html', context)

    #print(sorted(context['picked']))
    fortune_index = random.randint(0, len(context['available'])-1)
    fortune_id = context['available'][fortune_index]
    del context['available'][fortune_index]
    context['picked'].append(fortune_id)
    #print(fortune_id)
    fortune = Fortune.objects.get(pk=fortune_id)
    person = request.POST['person']
    if not person:
        person = 'Срамежливец [Shy]'
    context['count'] += 1
    kqsmet = person + ':\n' + fortune.fortune_text.replace('Б:','').rstrip('.') + '.\n[' + \
             fortune.english_text.replace('E:','').strip().rstrip('.') + '.]'
    context['already_picked_list'].insert(0, kqsmet)
    context['latest'] = "Късмет на " + kqsmet
    request.session['context'] = context
    return render(request, 'banitsa/index.html', context)

