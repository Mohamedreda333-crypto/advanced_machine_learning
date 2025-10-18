import requests
from bs4 import BeautifulSoup
import time
import csv

date = input('please enter the date in form of MM/DD/YYYY: ')
page = requests.get(F'https://www.yallakora.com/match-center?date={date}#days')
matches_details = []

def main (page):
    src = page.content
    soup = BeautifulSoup(src,"lxml")
    championships = soup.find_all("div",{'class':'matchesList'}) or soup.find_all("div",{'class':'matchCard'})
    
    def get_matches(championships):

        championship_title = championships.contents[1].find("h2").text.strip()
        all_matches = championships.contents[3].find_all("div",class_=["item", "finish", "liItem"])
        number_of_matches = len(all_matches)
        
        for i in range(number_of_matches):
            # get teams 
            team_a = all_matches[i].find("div",{'class':'teamA'}).text.strip()
            
            team_b = all_matches[i].find("div",{'class':'teamB'}).text.strip()
            
            matche_result = all_matches[i].find("div",{'class':'MResult'}).find_all("span",{'class':'score'})
            score_a = matche_result[0].text.strip()
            score_b = matche_result[1].text.strip()
            score = f"{score_a}-{score_b}"
            
            match_time = all_matches[i].find("div",{'class':'MResult'}).find("span",{'class':'time'}).text.strip()
            
            # add matches to matches_details list
            matches_details .append({
                "tournament": championship_title,
                "first team":team_a,
                "Second team":team_b,
                "score":score,
                "time":match_time   })

    for j in range(len(championships)):
        get_matches(championships[j])
        
    keys = matches_details[0].keys()
    with open ('E:/Yallakora_R/yallakora_matches.csv','w') as output_file:
        dict_writer = csv.DictWriter(output_file,keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        print('Done,File Created')
main (page)