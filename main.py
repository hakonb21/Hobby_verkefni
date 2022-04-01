from bs4 import BeautifulSoup
import requests
import os

UFC = requests.get('https://www.espn.com/mma/schedule/_/league/ufc')
BOX = requests.get('http://fightnights.com/upcoming-boxing-schedule')

UFC_SOUP = BeautifulSoup(UFC.text,'html.parser')
BOX_SOUP = BeautifulSoup(BOX.text, 'html.parser')



def clear_console():
    if os.name in ('nt', 'dos'):
        os.system('cls')
    else:
        os.system('clear')


def get_user_input():
    clear_console()
    user_input = input("Choose the sport (Ufc:Ufc, Box: Boxing): ")
    while True: 
        if user_input.lower() not in ['ufc','box']:
            print("Not a option")
            user_input = input("Choose the sport (Ufc:Ufc, Box: Boxing): ")
        else:
            return user_input.lower()


data = {
    "Maincard-fight": [], "Date" : "", 'Time': "", "Location" : ""
}


def get_boxing_fights():
    date_dict = {}
    fight_titles = BOX_SOUP.find_all('ul',class_ = 'event-list')
    for item in fight_titles:
        for i in item.find_all("span",class_ = 'month'):
            if len(i) < 4:
                date_dict[i] = i
    print(date_dict)


# def get_ufc_fights():
#     fight_list = []
#     ufc_fights = UFC_SOUP.find('div',class_ = 'Table__Scroller')
#     for info in ufc_fights:
#         for fight in info.find_all('tr',class_ = 'Table__TR Table__TR--sm Table__even'):
#             for card in fight.find_all('a',class_ = 'AnchorLink'):
#                 print(card.prettify())

def get_ufc_fights():
    link_lists = []
    fight_list = []
    ufc_fights = UFC_SOUP.find('table',class_ = 'Table')
    for line in ufc_fights.find_all('a',class_= 'AnchorLink'):
        link_lists.append(line.get('href'))
        fight_list.append(line.get_text())
    for i in fight_list:
        print(i)




def main():
    if get_user_input == 'ufc':
        get_ufc_fights()
    elif get_user_input == 'box':
        get_boxing_fights()

    
if __name__ == '__main__':
    pass

get_ufc_fights()
