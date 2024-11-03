from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def GetDataFromWeb(url, Data_Name):
    driver = webdriver.Chrome()
    driver.get(url)
    player_data = []
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content-part"]/section/div/div/div[1]/div/div[1]')))
        div = driver.find_element(By.XPATH, '//*[@id="content-part"]/section/div/div/div[1]/div/div[1]')

        rows = div.find_elements(By.TAG_NAME, 'tr')

        for row in rows[1:]:
            data = []
            # Lấy dữ liệu từ các cột
            cols = row.find_elements(By.TAG_NAME, 'td')
            for index, play in enumerate(cols):
                if index == 0:
                    HaiLuu = play.find_element(By.CLASS_NAME, "text")
                    a = HaiLuu.text.strip().split()
                    data.append(str(a[0]) + ' ' + str(a[1]))
                elif index == 1:
                    a = play.text.strip().split('\n')
                    data.append(a[0])
                    data.append(a[1])
                elif index == 2:
                    continue
                else:
                    data.append(play.text.strip())
            player_data.append(data)

    finally:
        driver.quit()
        print("Finish Page " + Data_Name)
    return player_data


url = 'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024'
Get_Player = GetDataFromWeb(url, '1')

for index in range(2, 19):
    x = GetDataFromWeb(url + '/' + str(index), str(index))
    Get_Player += x


import csv
from bai4.tieu_de import header

with open('E:/World/Code/Python/BTL/bai4/file/result.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for player in Get_Player:
        writer.writerow(player)
print("Exam 1 Success")
