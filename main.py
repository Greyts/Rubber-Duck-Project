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



def get_ducks(soup): # getting the ducks and amount sold

    try:
        is_duck = soup.find('h1').get_text().strip('<h1>')
    except:
        pass

    try:
        ducks_sold = soup.find('div', class_="_9a071_RRpJq _9a071_2sZmp _1h7wt").get_text().strip('<div>')
        print(ducks_sold)
    except:
        pass

    print(type(is_duck))
    print(is_duck)

def main(url):

    soup = get_page(url)
    get_ducks(soup)
    #print(soup)





if __name__ == '__main__':

    #url = 'https://allegro.pl/oferta/tullo-gumowe-kaczuszki-do-kapieli-4szt-zolte-012-9240757162?bi_s=ads&bi_m=listing%3Adesktop%3Aquery&bi_c=MDZlN2ExYWItOWE0Zi00N2QyLTg0YzQtMmQwNDAyNmY3YmZiAA&bi_t=ape&referrer=proxy&emission_unit_id=1e96e31a-c04a-4345-840b-dba0c3b83d2d'
    url = 'https://allegro.pl/oferta/kaczuszka-gumowa-zabawka-do-kapieli-20szt-za1163-9608879290?bi_s=ads&bi_m=listing%3Adesktop%3Aqueryandcategory&bi_c=NjVlZDlhMzAtNjNjOS00NzA4LThlZjctMDJmZWIxY2ZhY2Y1AA&bi_t=ape&referrer=proxy&emission_unit_id=0167525d-b7cc-44c1-892c-9e510a31ac62'

    main(url)