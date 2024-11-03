from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from player import Player
from player import Player_Manager
from player import Squad
from player import Squad_Manager

player_manager = Player_Manager()
squad_manager = Squad_Manager()

def validdata(n):
    if n == '': return "N/a"
    return float(n)

def GetDataFromWeb(url, Xpath_player, Xpath_squad, Data_Name):
    driver = webdriver.Chrome()
    driver.get(url)

    resultPlayerData = []
    resultSquadData = []
    try:
        time.sleep(10)
        table2 = driver.find_element(By.XPATH, Xpath_player)
        rows2 = table2.find_elements(By.TAG_NAME, 'tr')

        for row in rows2:  # Bỏ qua hàng tiêu đề
            cols = row.find_elements(By.TAG_NAME, 'td')
            data = []
            for id, play in enumerate(cols[:-1]):
                if id == 1:
                    a = play.text.strip().split()
                    if len(a) == 2:
                        data.append(a[1])
                    else:
                        data.append(play.text.strip())
                else:
                    s = play.text.strip()
                    if id >= 4:
                        s = s.replace(",", "")
                        s = validdata(s)
                    data.append(s)
            if len(data) != 0: resultPlayerData.append(data)


        table1 = driver.find_element(By.XPATH, Xpath_squad)
        rows1 = table1.find_elements(By.TAG_NAME, 'tr')

        for row in rows1[2:]:  # Bỏ qua hàng tiêu đề
            data = []
            name = row.find_element(By.TAG_NAME, 'th')
            data.append(name.text.strip())

            cols = row.find_elements(By.TAG_NAME, 'td')
            for id, value in enumerate(cols):
                s = value.text.strip()
                if id >= 4:
                    s = s.replace(",", "")
                    s = validdata(s)
                data.append(s)
            if len(data) != 0: resultSquadData.append(data)

    finally:
        driver.quit()
        print("Finish Page " + DataName)
    return resultPlayerData, resultSquadData


url = "https://fbref.com/en/comps/9/2023-2024/stats/2023-2024-Premier-League-Stats"
xpath_player = '//*[@id="stats_standard"]'
xpath_Squad = '//*[@id="stats_squads_standard_for"]'
DataName = "Standard"
list_player_result, list_Squad_result = GetDataFromWeb(url,xpath_player, xpath_Squad, DataName)

for i in list_player_result:
    p = player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p == None:
        new_p=Player(i[0],i[1],i[2],i[3],i[4])
        #bo qua i5 vi i5 la nam sinh
        new_p.setPlaying_time(i[6:9])
        #bo qua i9
        new_p.setPerformance([i[13],i[14],i[11],i[16],i[17]])
        new_p.setExpected(i[18:21])
        #bo qua i22
        new_p.setProgression(i[22:25])
        new_p.setPer90(i[25:])
        player_manager.add_Player(new_p)

player_manager.filtering()

#squad data
for i in list_Squad_result:
    s = squad_manager.findSquadByName(i[0])
    if s == None:
        new_s=Squad(*i[0:4])
        new_s.setPlaying_time(i[4:7])
        #bo qua i9
        new_s.setPerformance([i[11],i[12],i[9],i[14],i[15]])
        new_s.setExpected(i[16:19])
        #bo qua i22
        new_s.setProgression(i[20:22])
        new_s.setPer90(i[22:])
        squad_manager.add_Squad(new_s)



url = 'https://fbref.com/en/comps/9/2023-2024/keepers/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_keeper"]'
xpath_Squad = '//*[@id="stats_squads_keeper_for"]'
DataName = "Goalkeeping"
list_player_result, list_squad_result = GetDataFromWeb(url,xpath_player, xpath_Squad, DataName)

for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setGoalkeeping(i[10:20],i[20:])
#squad data
for i in list_squad_result:
    s=squad_manager.findSquadByName(i[0])
    if s!=None:
        s.setGoalkeeping(i[6:16],i[16:])



url = 'https://fbref.com/en/comps/9/2023-2024/shooting/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_shooting"]'
xpath_Squad = '//*[@id="stats_squads_shooting_for"]'
DataName = "Shooting"
list_player_result, list_squad_result = GetDataFromWeb(url,xpath_player, xpath_Squad, DataName)

for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setShooting(i[7:19],i[19:])
#squad data
for i in list_squad_result:
    s=squad_manager.findSquadByName(i[0])
    if s!=None:
        s.setShooting(i[3:15],i[15:])


url = 'https://fbref.com/en/comps/9/2023-2024/passing/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_passing"]'
xpath_Squad = '//*[@id="stats_squads_passing_for"]'
DataName = "Passing"
list_player_result, list_squad_result = GetDataFromWeb(url,xpath_player, xpath_Squad, DataName)

for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setPassing(i[7:12],i[12:15],i[15:18],i[18:21],i[21:])
#squad data
for i in list_squad_result:
    s=squad_manager.findSquadByName(i[0])
    if s!=None:
        s.setPassing(i[3:8],i[8:11],i[11:14],i[14:17],i[17:])



url = 'https://fbref.com/en/comps/9/2023-2024/passing_types/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_passing_types"]'
xpath_Squad = '//*[@id="stats_squads_passing_types_for"]'
DataName = "Pass Types"
list_player_result, list_squad_result = GetDataFromWeb(url,xpath_player, xpath_Squad, DataName)

for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setPassTypes(i[8:16],i[16:19],i[19:22])
#squad data
for i in list_squad_result:
    s=squad_manager.findSquadByName(i[0])
    if s!=None:
        s.setPassTypes(i[4:12],i[12:15],i[15:])




url = 'https://fbref.com/en/comps/9/2023-2024/gca/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_gca"]'
xpath_Squad = '//*[@id="stats_squads_gca_for"]'
DataName = "Goal and Shot Creation"
list_player_result, list_squad_result = GetDataFromWeb(url,xpath_player, xpath_Squad, DataName)


for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setGoalShotCreation(i[7:9],i[9:15],i[15:17],i[17:23])
#squad data
for i in list_squad_result:
    s=squad_manager.findSquadByName(i[0])
    if s!=None:
        s.setGoalShotCreation(i[3:5],i[5:11],i[11:13],i[13:])




url = 'https://fbref.com/en/comps/9/2023-2024/defense/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_defense"]'
xpath_Squad = '//*[@id="stats_squads_defense_for"]'
DataName = "Defensive Actions"
list_player_result, list_squad_result = GetDataFromWeb(url,xpath_player, xpath_Squad, DataName)

for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setDefensiveActions(i[7:12],i[12:16],i[16:23])
#squad data
for i in list_squad_result:
    s=squad_manager.findSquadByName(i[0])
    if s!=None:
        s.setDefensiveActions(i[3:8],i[8:12],i[12:])




url = 'https://fbref.com/en/comps/9/2023-2024/possession/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_possession"]'
xpath_Squad = '//*[@id="stats_squads_possession_for"]'
DataName = "Possession"
list_player_result, list_squad_result = GetDataFromWeb(url,xpath_player, xpath_Squad, DataName)

for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setPossession(i[7:14],i[14:19],i[19:27],i[27:29])
#squad data
for i in list_squad_result:
    s=squad_manager.findSquadByName(i[0])
    if s!=None:
        s.setPossession(i[4:11],i[11:16],i[16:24],i[24:26])



url = 'https://fbref.com/en/comps/9/2023-2024/playingtime/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_playing_time"]'
xpath_Squad = '//*[@id="stats_squads_playing_time_for"]'
DataName = "Playing Time"
list_player_result, list_squad_result = GetDataFromWeb(url,xpath_player, xpath_Squad, DataName)

for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setPlayingTimeDetail(i[11:14],i[14:17],i[17:20],i[23:25])
#squad data
for i in list_squad_result:
    s=squad_manager.findSquadByName(i[0])
    if s!=None:
        s.setPlayingTimeDetail(i[8:11],i[11:14],i[14:17],i[19:21])



url = 'https://fbref.com/en/comps/9/2023-2024/misc/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_misc"]'
xpath_Squad = '//*[@id="stats_squads_misc_for"]'
DataName = "Miscellaneous"
list_player_result, list_squad_result = GetDataFromWeb(url,xpath_player, xpath_Squad, DataName)


for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setMiscStats(i[10:14]+i[18:20],i[20:23])
#squad data
for i in list_squad_result:
    s=squad_manager.findSquadByName(i[0])
    if s!=None:
        s.setMiscStats(i[6:10]+i[14:16],i[16:])

player_manager.sortingByName()





import csv
from bai1.tieu_de import header, row

with open('E:/World/Code/Python/BTL/bai1/file/result.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)

    for player in player_manager.list_player:
        r = row(player)
        writer.writerow(r)
print("Exam 1 Success")


from bai1.tieu_de import header2, row2

with open('E:/World/Code/Python/BTL/bai1/file/result2.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header2)

    for squad in squad_manager.list_squad:
        r = row2(squad)
        writer.writerow(r)
print("Exam 1 Success")