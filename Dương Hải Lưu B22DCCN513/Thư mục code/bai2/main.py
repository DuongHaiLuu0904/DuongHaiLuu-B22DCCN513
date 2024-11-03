import os
import pandas as pd
import matplotlib.pyplot as plt
import math


def read_player_data_from_txt(file_path):
    players = []
    with open(file_path, 'r', encoding='utf-8') as file:
        # Bỏ qua dòng tiêu đề
        header = file.readline().strip().split("\t")

        # Đọc từng dòng dữ liệu
        for line in file:
            # Tách các giá trị bằng dấu tab và thêm vào danh sách
            values = line.strip().split("\t")
            players.append(values)
    return players

# Sử dụng hàm để đọc dữ liệu cầu thủ từ file player_data.txt
player_data = read_player_data_from_txt('E:/World/Code/Python/BTL/bai1/file/player_data.txt')

from tieu_de import header
from max_min_player import *

list_mm = max_min()

for index, value in enumerate(header):
    if index < 3: continue
    player_data = sorted(player_data, key=lambda x: x[index])
    list_mm.add_max_min([value, player_data[0][0], player_data[1][0], player_data[2][0],
                         player_data[-3][0],player_data[-2][0], player_data[-1][0]])


import openpyxl
# Lưu dữ liệu vào file Excel cho player_manager
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Players"

# Ghi tiêu đề (header)
ws.append(header_max_min)
# Ghi dữ liệu của các cầu thủ
for player in list_mm.list_max_min:
    ws.append(player)

# Lưu vào file Excel
wb.save('E:/World/Code/Python/BTL/bai2/file/result.xlsx')
print("Exam 1 Success - Player Data Saved")




# Tải dữ liệu từ file CSV vào DataFrame df
df = pd.read_csv('E:/World/Code/Python/BTL/bai2/file/result.csv')

def add_statistics_for_team(team_name, numeric_df, table):
    table['Team'].append(team_name)
    for att in numeric_df.columns:
        table['Median of ' + att].append(float(numeric_df[att].median()))
        table['Mean of ' + att].append(float(numeric_df[att].mean()))
        table['Std of ' + att].append(float(numeric_df[att].std()))

numeric_df = df.select_dtypes(include=['float', 'int'])
# Tạo dictionary để lưu kết quả
table = {'Team': []}
# Khởi tạo các cột cho Median, Mean, Std của từng thuộc tính số
for att in numeric_df.columns:
    table['Median of ' + att] = []
    table['Mean of ' + att] = []
    table['Std of ' + att] = []
    # Tính toán cho tất cả các đội (team 'all')
add_statistics_for_team('all', numeric_df, table)
teams=['all']
teams.extend(df['team'].unique())

    # Tính toán cho từng đội
for team in teams[1:]:
        # Bỏ qua 'all' vì đã tính toán trước
    filtered_df = df[df['team'] == team]
    numeric_df = filtered_df.select_dtypes(include=['float', 'int'])
    add_statistics_for_team(team, numeric_df, table)
  # Tạo DataFrame từ dictionary 'table'
result2 = pd.DataFrame(table)

    # lưu vào result2.csv
result2.to_csv('E:/World/Code/Python/BTL/bai2/file/result2.csv', index=False)







# Đọc dữ liệu
df = pd.read_csv('E:/World/Code/Python/BTL/bai2/file/result.csv')

# Tạo thư mục để lưu biểu đồ nếu chưa tồn tại
output_folder = 'E:/World/Code/Python/BTL/bai2/output_histograms'
os.makedirs(output_folder, exist_ok=True)

# Vẽ histogram cho toàn bộ giải đấu
numeric_df = df.select_dtypes(include=['float', 'int'])
num_attributes = len(numeric_df.columns)
num_cols = 4
num_rows = math.ceil(num_attributes / num_cols)

plt.figure(figsize=(16, 10))  # Tăng chiều cao
for idx, att in enumerate(numeric_df.columns, 1):
    plt.subplot(num_rows, num_cols, idx)
    plt.hist(numeric_df[att], bins=10, alpha=0.7, color='blue', edgecolor='black')
    plt.title(f'Histogram of {att} (All Teams)', fontsize=10)  # Giảm kích thước font tiêu đề
    plt.xlabel(att, fontsize=8)  # Giảm kích thước font nhãn
    plt.ylabel('Frequency', fontsize=8)  # Giảm kích thước font nhãn
    plt.grid(axis='y', alpha=0.75)

plt.subplots_adjust(hspace=0.5, wspace=0.3)  # Điều chỉnh khoảng cách giữa các ô con
plt.savefig(os.path.join(output_folder, 'all_teams_histogram.png'))
plt.close()

# Vẽ histogram cho từng đội
teams = df['team'].unique()
for team in teams:
    team_df = df[df['team'] == team].select_dtypes(include=['float', 'int'])
    num_attributes_team = len(team_df.columns)
    num_rows_team = math.ceil(num_attributes_team / num_cols)

    plt.figure(figsize=(16, 10))  # Tăng chiều cao
    for idx, att in enumerate(team_df.columns, 1):
        plt.subplot(num_rows_team, num_cols, idx)
        plt.hist(team_df[att], bins=10, alpha=0.7, color='green', edgecolor='black')
        plt.title(f'Histogram of {att} ({team})', fontsize=10)  # Giảm kích thước font tiêu đề
        plt.xlabel(att, fontsize=8)  # Giảm kích thước font nhãn
        plt.ylabel('Frequency', fontsize=8)  # Giảm kích thước font nhãn
        plt.grid(axis='y', alpha=0.75)

    plt.subplots_adjust(hspace=0.5, wspace=0.3)  # Điều chỉnh khoảng cách giữa các ô con
    plt.savefig(os.path.join(output_folder, f'{team}_histogram.png'))
    plt.close()







df2 = pd.read_csv('E:/World/Code/Python/BTL/bai2/file/result2.csv')
df2.drop(index=0, inplace=True)
numeric_columns = df2.select_dtypes(include=['float', 'int']).columns

# Tạo danh sách để lưu kết quả cho mỗi thuộc tính
highest_team_per_stat = []

for column in numeric_columns:
    # Tìm chỉ số dòng có giá trị lớn nhất cho thuộc tính
    max_idx = df2[column].idxmax()

    # Lấy tên đội bóng và giá trị của thuộc tính tại chỉ số này
    max_team = df2.loc[max_idx, 'Team']
    max_score = df2.loc[max_idx, column]

    # Thêm kết quả vào danh sách
    highest_team_per_stat.append({
        'Attribute': column,
        'Team': max_team,
        'Highest Score': max_score
    })

# Chuyển đổi danh sách kết quả thành DataFrame
highest_team_per_stat_df = pd.DataFrame(highest_team_per_stat)

    # lưu vào result3.csv
highest_team_per_stat_df.to_csv('E:/World/Code/Python/BTL/bai2/file/result3.csv', index=False)



# đếm  xem mỗi đội bóng có bao nhiêu chỉ số điểm cao nhất
print(highest_team_per_stat_df['Team'].value_counts())