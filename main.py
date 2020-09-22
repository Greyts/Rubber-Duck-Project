import requests
from bs4 import BeautifulSoup
from get_url import *
import re

def ducks_in(is_duck: str):  # checks how many ducks are sold in packages

    string = ''
    ducks = 1

    try:
        if 'szt' or 'sztuk' in is_duck.lower():
            split = is_duck.split()

            for word in split:
                if 'szt' in word.lower():
                    digits = [i for i in word if i.isdigit()]

                    for digit in digits:
                        string += digit

                    ducks = int(string)
                    break

                elif word.isdigit():
                    try:
                        digit = word + (split[split.index(word) + 1])
                    except IndexError:
                        break

                    if 'szt' or 'sztuk' in digit.lower():
                        digits = [i for i in word if i.isdigit()]

                        for digit in digits:
                            string += digit

                        ducks = int(string)
                        break

    except:
        pass

    return ducks


def ducks_total(string_sold: str, ducks_together: int): #strips string to return integer of sold ducks (multiplies sold sets by amount of ducks in a single package)

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



def get_ducks(soup, page): # getting the ducks and amount sold

    try:
        is_duck = soup.find('h1').get_text().strip('<h1>')
    except:
        pass

    try:
        ducks_sold = soup.find('div', class_="_9a071_RRpJq _9a071_2sZmp _1h7wt").get_text().strip('<div>')

    except:
        ducks_sold = 0

    ducks_together = (ducks_in(is_duck))
    total_ducks = ducks_total(ducks_sold, ducks_together)

    data = {
        'title': is_duck,
        'sold' : total_ducks,
        'ducks sold together' : ducks_together,
        'link' : page
    }

    print(data)

    return data

def main(url):

    soup = get_page(url)
    try:
        number_of_pages = get_number_of_pages(soup)
    except:
        number_of_pages = 1



    for x in range(int(number_of_pages)+1):

        try:
            links = get_list_of_pages(get_multiple_pages(f'{url}{x+1}'))
            print(f'{url}{x+1}')
            for page in links:
                soup = get_page(page)
                ducks = get_ducks(soup, page)
        except:
            pass

    return ducks

if __name__ == '__main__':

    url = 'https://allegro.pl/kategoria/zabawki-do-kapieli-19416?string=kaczuszka%20gumowa&bmatch=baseline-product-eyesa2-engag-dict45-bab-1-3-0717&p='
    main(url)

    # for x in range(number_of_pages+1): # in range(99) aims to scout trough all the pages available until every single page has been searched  TRZEBA NAPRAWIć BO SIĘ ZAPĘTLA
    #     try:
    #         links = get_list_of_pages(get_multiple_pages(f'{url}{x}'))
    #
    #         for url in links:
    #             main(url)
    #
    #     except:
    #         pass