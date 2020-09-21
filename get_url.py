import requests
from bs4 import BeautifulSoup

def get_multiple_pages(url): # preparing the soup out of the search outcome

    result = requests.get(url)

    if not result.ok: # checking if the page responded
        print('Server responded: ', result.status_code)
    else:
        print('Server responded correctly: ', result.status_code)
        soup = BeautifulSoup(result.text, 'lxml')
    return soup

def get_list_of_pages(soup): # puts all the links to each posting in a list

    try:
        posting = soup.find_all('', class_='_w7z6o _uj8z7 meqh_en mpof_z0 mqu1_16 _9c44d_2vTdY')#.strip('<a>')
        links = [link.get('href') for link in posting]

    except:
        links = []

    return links

if __name__ == '__main__':


    soup = get_multiple_pages('https://allegro.pl/kategoria/zabawki-do-kapieli-19416?string=kaczuszka%20gumowa&bmatch=baseline-product-eyesa2-engag-dict45-bab-1-3-0717')
    get_list_of_pages(soup)