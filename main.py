from bs4 import BeautifulSoup
import requests

UFC = requests.get('https://www.espn.com/mma/schedule/_/league/ufc')
BOX = requests.get('http://fightnights.com/upcoming-boxing-schedule')

UFC_SOUP = BeautifulSoup(UFC.text,'html.parser')
BOX_SOUP = BeautifulSoup(BOX.text, 'html.parser')



def get_user_input():
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
    fight_titles = BOX_SOUP.find_all('div',)

def get_ufc_fights():
    pass


def main():
    if get_user_input == 'ufc':
        get_ufc_fights()
    elif get_user_input == 'box':
        get_boxing_fights()

    
if __name__ == '__main__':
    pass



