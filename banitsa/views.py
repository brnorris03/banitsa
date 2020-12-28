from django.http import HttpResponse
from django.shortcuts import render
import random

from .models import Fortune

def index(request):
    if not 'context' in request.session.keys():
        context = {'picked': [], 'already_picked_list': [], 'final': False, 'latest': None,
                   'count': 0, 'total': Fortune.objects.count()}
        request.session['context'] = context
        request.session.set_expiry(7200)
    else:
        context = request.session['context']
    return render(request, 'banitsa/index.html', context)

def pick(request):
    context = request.session['context']
    if context['final']:
        return render(request, 'banitsa/index.html', context)
    num_fortunes = context['total']
    if len(context['picked']) >= num_fortunes:
        context['final'] = True
        request.session['context'] = context
        return render(request, 'banitsa/index.html', context)

    fortune_id = random.randint(0, num_fortunes - 1)
    while fortune_id in context['picked']:
        fortune_id = random.randint(0,num_fortunes-1)
    context['picked'].append(fortune_id)
    fortune = Fortune.objects.get(pk=fortune_id)
    person = request.POST['person']
    if not person:
        person = 'Срамежливец/Shy'
    context['count'] += 1
    kqsmet = person + ': ' + fortune.fortune_text.replace('Б:','').rstrip('.') + '. [' + \
             fortune.english_text.replace('E:','').rstrip('.') + '.]'
    context['already_picked_list'].insert(0, kqsmet)
    context['latest'] = "Късмет на " + kqsmet
    request.session['context'] = context
    return render(request, 'banitsa/index.html', context)

