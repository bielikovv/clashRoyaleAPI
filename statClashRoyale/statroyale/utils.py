import requests

def get_profile_info(tag):
    HEADERS = {'Authorization': 'Bearer YOUR_API_KEY'}
    url = 'https://api.clashroyale.com/v1/players/%23{}/'
    data = requests.get(url.format(tag), headers=HEADERS).json()
    return data



def get_last_chest_info(tag):
    HEADERS = {'Authorization': 'Bearer YOUR_API_KEY'}
    url = 'https://api.clashroyale.com/v1/players/%23{}/upcomingchests/'
    data = requests.get(url.format(tag), headers=HEADERS).json()
    return data



def get_arena(arena, trophies):
    if trophies < 5000:
        return arena
    if 5000 <= trophies < 5300:
        return 15
    elif 5300 <= trophies < 5600:
        return 16
    elif 5600 <= trophies < 6000:
        return 17
    elif 6000 <= trophies < 6300:
        return 18
    elif 6300 <= trophies < 6600:
        return 19
    elif 6600 <= trophies < 7000:
        return 20
    elif 7000 <= trophies < 7300:
        return 21
    elif 7300 <= trophies < 7600:
        return 22
    elif 7600 <= trophies < 8000:
        return 23
    elif 8000 <= trophies:
        return 24


def add_chest_icon(chests):
    for item in chests['items']:
        if item['name'] == 'Golden Chest':
            item.update({'icon': 'https://cdn.royaleapi.com/static/img/chests-fs8/128x128/chest-golden-fs8.png?v=4'})
        elif item['name'] == 'Silver Chest':
            item.update({'icon': 'https://cdn.royaleapi.com/static/img/chests-fs8/128x128/chest-silver-fs8.png?v=4'})
        elif item['name'] == 'Magical Chest':
            item.update({'icon': 'https://cdn.royaleapi.com/static/img/chests-fs8/128x128/chest-magical-fs8.png?v=4'})
        elif item['name'] == 'Giant Chest':
            item.update({'icon': 'https://cdn.royaleapi.com/static/img/chests-fs8/128x128/chest-giant-fs8.png?v=4'})
        elif item['name'] == 'Legendary Chest':
            item.update({'icon': 'https://cdn.royaleapi.com/static/img/chests-fs8/128x128/chest-legendary-fs8.png?v=4'})
        elif item['name'] == 'Mega Lightning Chest':
            item.update(
                {'icon': 'https://cdn.royaleapi.com/static/img/chests-fs8/128x128/chest-megalightning-fs8.png?v=4'})
        elif item['name'] == 'Epic Chest':
            item.update({'icon': 'https://cdn.royaleapi.com/static/img/chests-fs8/128x128/chest-epic-fs8.png?v=4'})
    return chests
