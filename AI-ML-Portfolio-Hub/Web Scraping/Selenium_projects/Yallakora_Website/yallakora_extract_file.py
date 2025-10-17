from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
import csv


# Format the date as dd-mm-yyyy
start_date_str = input("Enter start date (MM/DD/YYYY): ")
end_date_str = input("Enter end date (MM/DD/YYYY): ")

start_date = datetime.strptime(start_date_str, "%m/%d/%Y")
end_date = datetime.strptime(end_date_str, "%m/%d/%Y")


dates = []
while start_date <= end_date:
    dates.append(start_date.strftime("%m/%d/%Y"))
    # Add one day to the current date
    start_date += timedelta(days=1) 
 

def yallakorra(link, date):
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get(link)
    time.sleep(5)

    matchs_list = browser.find_elements('class name', 'matchCard')
    time.sleep(3)

    matches_data = []

    for block in matchs_list:
        html_code = block.get_attribute('outerHTML')
        soup = BeautifulSoup(html_code, 'html.parser')

        # Extract championship name
        championship_tag = soup.find("a", {"class": "tourTitle"})
        championship = championship_tag.find("h2").text.strip() if championship_tag and championship_tag.find("h2") else "No championship found"

        # Extract all matches in championships
        matches = soup.find_all("div", class_=["item", "finish", "liItem"])
        for match in matches:
            # Extract first team name of each matches in championships
            team_A = match.find("div", {"class": "teams teamA"})
            first_team = team_A.find("p").text.strip() if team_A and team_A.find("p") else 'N/A'
            
            # Extract second team name of each matches in championships
            team_B = match.find("div", {"class": "teams teamB"})
            second_team = team_B.find("p").text.strip() if team_B and team_B.find("p") else 'N/A'

            match_results = match.find("div", {'class':'MResult'})
            if match_results:
                scores = match_results.find_all("span", {'class':'score'})
                if len(scores) >= 2:
                    scoreA = scores[0].text.strip()
                    scoreB = scores[1].text.strip()
                else:
                    scoreA = scoreB = "-"
                    
                # Extract Result of each matches in championships
                result = f"{scoreA}-{scoreB}"

                time_ = match_results.find("span", {"class": "time"})
                # Extract Time of each matches in championships
                match_time = time_.text.strip() if time_ else "N/A"
            else:
                result = "N/A"
                match_time = "N/A"
                
            # Extract Time of each matches in championships
            Round_tag = match.find("div", {'class':"date"})
            round_name = Round_tag.text.strip() if Round_tag else "N/A"


            match_info = {
                "date": date,
                "tournament": championship,
                "round": round_name,
                "team1": first_team,
                "team2": second_team,
                "score": result,
                "time": match_time
            }

            matches_data.append(match_info)

    browser.quit()
    return matches_data

# collect all days in one list
all_matches = []
for date in dates:
    print(f"Scraping matches for {date} ...")
    url = f"https://www.yallakora.com/match-center?date={date}"
    day_matches = yallakorra(url, date)
    all_matches.extend(day_matches)
    print(all_matches)
    print(f"Done {date} ({len(day_matches)} matches)")

# save all Data as CSV file
path = 'E:/Yallakora/yallakora_matches.csv'
with open(path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=all_matches[0].keys())
    writer.writeheader()
    writer.writerows(all_matches)

print("\n✅ All matches saved in 'yallakora_matches.csv'")
