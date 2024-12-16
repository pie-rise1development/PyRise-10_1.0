import requests

def download_music():
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;;q=0.7,fi;q=0.6,nb;q=0.5,is;q=0.4,pt;q=0.3,ro;q=0.2,it;q=0.1,de;q=0.1',
        'Connection': 'keep-alive',
        'Referer': 'https://music.yandex.ru/chart',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'X-Current-UID': '403036463',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Repath-Y': 'https://music.yandex.ru/chart',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    params = {
        'what': 'chart',
        'lang': 'ru',
        'external-domain': 'music.yandex.ru',
        'everembed': 'false',
        'ncrnd': '0.23800355071570123',
    }

    try:
        responce = requests.get('https://music.yandex.ru/handlers/main.jsx', params=params, headers=headers)
        responce.raise_for_status() # Проверка на ошибки HTTP.
        chart = responce.json().get('chartPositions', [])

        if not chart:
            print("Не удалось получить данные о чартах.")
            return
        
        result = []
        for track in chart[:7]:
            position = track['track']['chart']['position']
            title = track['track']['title']
            author = track['track']['artists'][0]['name']
            result.append(f"№{position}: {author} - {title}")

            print("Здравствуйте! На данный момент в чартах песен имеются такие ✨:")
            for idx, track_info in enumerate(result):
                medal = ["🥇", "🥈", "🥉"][idx] if idx < 3 else "   "
                print(f"{medal}{track_info}")

    except requests.RequestException as e:
        print(f"Ошибка! Произошла ошибка и вот её код: {e}")
    except ValueError as e:
        print(f"Ошибка обработки данных: {e}")

if __name__ == "__main__":
    download_music()