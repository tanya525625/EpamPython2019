import requests


class PikabuGrabber():
    HOME = "https://pikabu.ru/"
    HEADERS = {
        "Host": "pikabu.ru",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:67.0) Gecko/20100101 Firefox/67.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://pikabu.ru/@tanya7492401",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "Trailers"
    }

    def __init__(self, username, password):
        self.session = requests.Session()
        self.session.headers = self.HEADERS
        self.auth(username, password)

    def auth(self, username, password):
        get = self.session.get(self.HOME)
