import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Battle_of_the_Bulge'
# response = requests.get(URL)
# print(dir(response))
# soup = BeautifulSoup(content, 'html.parser')

# print('hello?')

def get_citations_needed_count(URL):
    """takes in a URL and returns an int of how many times <a> 'citation needed' occurs"""
    # print('top count')
    response = requests.get(URL)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser') #converts to soup object
    result = soup.find_all('a', href="/wiki/Wikipedia:Citation_needed") #looks for <a>
    # print('bottom count')
    print(len(result)) # number of links it finds
    return len(result)

def get_citations_needed_report(URL):
    """takes in a URL and returns paragraph where citation is needed"""
    # print('top report')
    response = requests.get(URL)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result = soup.find_all('a', href="/wiki/Wikipedia:Citation_needed")

    dictionary = []

    for link in result:
        P = link.parent.parent.parent
        P = P.text.strip()
        dictionary.append(P)

    # print('above dictionary')
    for P in dictionary:
        print(P, sep='\n')
        print('\n')

    return dictionary

#for me to see in command line
if __name__ == "__main__":
    URL = 'https://en.wikipedia.org/wiki/Battle_of_the_Bulge'
    get_citations_needed_count(URL)
    get_citations_needed_report(URL)
