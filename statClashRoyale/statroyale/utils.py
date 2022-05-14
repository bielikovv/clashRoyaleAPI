import requests

def get_profile_info(tag):
    HEADERS = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjEyODA4MzRmLTk3ZDgtNDM3MS04NWM4LTY5YTY4MWYxNmY5YyIsImlhdCI6MTY1MjQ0MzE5Niwic3ViIjoiZGV2ZWxvcGVyLzYyY2ZkM2IyLTA3OGMtZmZlZS1hZjUzLWY2MmQxMjViOTk0OSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxMDkuMjA3LjExOC4xNjgiXSwidHlwZSI6ImNsaWVudCJ9XX0.4Oo9-BKHv2kFUKc2pjYSKa1LQe9kjw5kQ7J-Of2cVJWNHTi_fVgwOkW7Gp5MGH0NPcZrywnwJX1nUnAv9d4n2w'}
    url = 'https://api.clashroyale.com/v1/players/%23{}/'
    data = requests.get(url.format(tag), headers=HEADERS).json()
    return data



def get_last_chest_info(tag):
    HEADERS = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjEyODA4MzRmLTk3ZDgtNDM3MS04NWM4LTY5YTY4MWYxNmY5YyIsImlhdCI6MTY1MjQ0MzE5Niwic3ViIjoiZGV2ZWxvcGVyLzYyY2ZkM2IyLTA3OGMtZmZlZS1hZjUzLWY2MmQxMjViOTk0OSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxMDkuMjA3LjExOC4xNjgiXSwidHlwZSI6ImNsaWVudCJ9XX0.4Oo9-BKHv2kFUKc2pjYSKa1LQe9kjw5kQ7J-Of2cVJWNHTi_fVgwOkW7Gp5MGH0NPcZrywnwJX1nUnAv9d4n2w'}
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
