# parašykite funkciją, kuri į args priimtų url eilučių sąrašą ir grąžintų, kokį serverį naudoja svetainė.

import requests


def server_name(*links):
    for link in links:
        response = requests.get(link)
        if response.ok:
            try:
                link_server = response.headers['server']
                print(f'URL: {link}   Server: {link_server}')
            except KeyError:
                print(f'URL: {link}   Server: {None}')

servers = ("https://www.w3schools.com/python/python_regex.asp", "https://www.httpbin.org/",
            "https://www.kaina24.lt/s/nzxt-140mm/",
            "https://www.delfi.lt/news/daily/lithuania/kodel-asmens-kodas-prasideda-5-arba-6-13577734")
server_name(*servers)
