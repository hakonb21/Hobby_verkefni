from bs4 import BeautifulSoup
import requests
import os
from datetime import date as DATE

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


def get_boxing_fights():
    fight_list = []
    datelisTemp = []
    date_list = []
    fight_titles = BOX_SOUP.find_all('ul',class_ = 'event-list')
    for item in fight_titles:
        for i in item.find_all('h2',class_ = 'title'):
            fight_list.append(i.get_text())
        for j in item.find_all('span',class_= 'month'):
            datelisTemp.append(j.get_text())
    for month in datelisTemp[::2]:
        for day in datelisTemp[1::2]:
            date_list.append(month + day)
    return fight_list,date_list

def print_boxing():
    fight_list,date_list = get_boxing_fights()

    for fight, date in zip(fight_list,date_list):
        print(f"Main event: {fight} on date: {date} \n")


def get_ufc_fights():
    fight_list = []
    date_list = []
    ufc_fights = UFC_SOUP.find('table',class_ = 'Table')
    for line in ufc_fights.find_all('a',class_= 'AnchorLink'):
        if len(line.get_text()) > 2:
            if line.get_text().split()[1] in ['PM','AM']:
                pass
            else:
                fight_list.append(line.get_text())
    for j in ufc_fights.find_all('span',class_ = 'date__innerCell'):
        date_list.append(j.get_text())
    return fight_list,date_list

def ufc_printer():
    data = {}
    fight_list, date_list = get_ufc_fights()
    for fight,date in zip(fight_list,date_list):
        data[fight] = date
    for key,value in data.items():
        print(f"Main event: {key} on date: {value}\n")

def write_to_file(fightlis,datelis,sport):
    with open('data.json','w') as f:
        f.write(f"\nUpcoming {sport} fights on {DATE.today()}")
        for fight,date in zip(fightlis,datelis):
            f.write(f"  Main event: {fight} on date: {date}\n")


def main():
    a = get_user_input()
    clear_console()
    if a == 'ufc':
        ufc_printer()
        fight_lis,date_lis = get_ufc_fights()
        write_to_file(fight_lis,date_lis,'UFC')
    elif a == 'box':
        print_boxing()
        fight_lis,date_lis = get_boxing_fights()
        write_to_file(fight_lis,date_lis,'Boxing')
        

    
if __name__ == '__main__':
    main()


