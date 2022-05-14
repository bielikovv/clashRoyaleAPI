from django.shortcuts import render, redirect
from django.views.generic import View
from .utils import *

def show_main_page(request):
    return render(request, 'statroyale/main_page.html')



class GetProfileStatistics(View):
    def get(self, request, tag):
        data = get_profile_info(tag)
        if 'reason' in data:
            if data['reason'] == 'notFound':
                return redirect('main_page')

        main_info = {
            'name': data['name'],
            'tag': data['tag'],
            'level': data['expLevel'],
            'trophies': data['trophies'],
            'best_trophies': data['bestTrophies'],
            'arena': data['arena']['name'][-1:],
            'clan_name': data['clan']['name'],
            'wins': data['wins'],
            'losses': data['losses'],
            'currentDeck': data['currentDeck'],
            'w_l_stat': round(float(data['wins']) / float(data['losses']), 2)
        }
        main_info['arena'] = get_arena(main_info['arena'], main_info['trophies'])

        chests = get_last_chest_info(tag)
        chests = add_chest_icon(chests)
        for item in chests['items']:
            item['index'] = int(item['index']) + 1
        return render(request, 'statroyale/profile_stat.html', {'info':main_info, 'chests':chests['items'], 'name': data['name']})




