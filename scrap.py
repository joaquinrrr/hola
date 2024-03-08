#video from yt https://www.youtube.com/watch?v=YjpGdFwIAxg
#page: https://offshoreleaks.icij.org/search?q=Peru&c=&j=&d=

from requests_html import HTMLSession

# Inicia una sesión HTML
s = HTMLSession()

# Define la URL
url = 'https://offshoreleaks.icij.org/power-players.json'

# Define los encabezados
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'terms.accept=1; _ga_ZHK7PVGCC7=GS1.1.1709565051.1.1.1709565469.60.0.0; _gid=GA1.2.1419783051.1709734718; _gat_gtag_UA_3383794_9=1; _ga_PJ4Y19JL7T=GS1.1.1709740028.7.1.1709740079.9.0.0; _ga=GA1.1.1521487024.1709242262',
    'Host': 'offshoreleaks.icij.org',
    'If-None-Match': 'W/"abd7997af445bf71f26ac3018c641f24"',
    'Referer': 'https://offshoreleaks.icij.org/nodes/85028241',
    'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}



# Hace una solicitud GET a la URL con los encabezados definidos
r = s.get(url, headers=headers, verify=False)

# Imprime el contenido de la página
print(r.text)

'''r = s.get(url)

table = r.html.find('table')[0]

for row in table.find('tr'):
  for c in row.find('td'):
    print(c.text)

tabledata = [[c.text for c in row.find('td')[:-1]] for row in table.find('tr')][1:]
tableheaders = [[c.text for c in row.find('th')[:-1]] for row in table.find('tr')][0]

res = [dict(zip(tableheaders,t)) for t in tabledata]

with open('table.json','w') as f:
  json.dump(res,f) '''