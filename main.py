import requests
from bs4 import BeautifulSoup

def ducks_in(is_duck: str): #checks how many ducks are sold together

    string =''
    try:
        if 'szt' or 'sztuk' in is_duck:

            for word in is_duck.split():

                if 'sz'.lower() in word:

                    digits = [i for i in word if i.isdigit()]

                    for digit in digits:
                        string += digit

                    ducks = int(string)
        else:
            ducks = 1
    except:
        ducks = 1

    return ducks


def ducks_total(string_sold: str, ducks_together: int): #strips string to return integer of sold ducks

    try:
        digits =[digit for digit in string_sold.split() if digit.isdigit()]
        sold_packages = int(digits[-1])
    except:
        sold_packages = 0

    return sold_packages * ducks_together

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
        print(type(ducks_sold))
    except:
        pass

    ducks_together = (ducks_in(is_duck))
    total_ducks = ducks_total(ducks_sold, ducks_together)

    data = {
        'title': is_duck,
        'sold' : total_ducks,
        'ducks sold together' : ducks_together
    }

    print(data)

    return data

def main(url):

    soup = get_page(url)
    get_ducks(soup)



if __name__ == '__main__':

    #url = 'https://allegro.pl/oferta/tullo-gumowe-kaczuszki-do-kapieli-4szt-zolte-012-9240757162?bi_s=ads&bi_m=listing%3Adesktop%3Aquery&bi_c=MDZlN2ExYWItOWE0Zi00N2QyLTg0YzQtMmQwNDAyNmY3YmZiAA&bi_t=ape&referrer=proxy&emission_unit_id=1e96e31a-c04a-4345-840b-dba0c3b83d2d'
    #url = 'https://allegro.pl/oferta/kaczuszka-gumowa-zabawka-do-kapieli-20szt-za1163-9608879290?bi_s=ads&bi_m=listing%3Adesktop%3Aqueryandcategory&bi_c=NjVlZDlhMzAtNjNjOS00NzA4LThlZjctMDJmZWIxY2ZhY2Y1AA&bi_t=ape&referrer=proxy&emission_unit_id=0167525d-b7cc-44c1-892c-9e510a31ac62'
    url = 'https://allegro.pl/oferta/gumowa-kaczka-kaczuszka-zabawka-do-kapieli-biala-9553447581'
    main(url)
