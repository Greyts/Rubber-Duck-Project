import requests
from bs4 import BeautifulSoup



def get_page(url): # preparing the soup

    result = requests.get(url)

    if not result.ok: # checking if the page responded
        print('Server responded: ', result.status_code)
    else:
        print('Server responded correctly: ', result.status_code)
        soup = BeautifulSoup(result.text, 'lxml')
    return soup

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

def get_number_of_pages(soup): # determines number of pages

    try:
        number_of_pages = soup.find('span', class_="_1h7wt _1fkm6 _g1gnj _3db39_3i0GV _3db39_XEsAE").get_text().strip('span')
    except:
        number_of_pages = 0

    return number_of_pages

if __name__ == '__main__':


    soup = get_multiple_pages('https://allegro.pl/kategoria/zabawki-do-kapieli-19416?string=kaczuszka%20gumowa&bmatch=baseline-product-eyesa2-engag-dict45-bab-1-3-0717&p=1')
    # get_list_of_pages(soup)
    print(get_number_of_pages(soup))
