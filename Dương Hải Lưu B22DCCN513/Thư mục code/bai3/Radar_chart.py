import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def create_radar_chart(ax, player, attributes):

    df = pd.read_csv(args.file)

    # Lấy dữ liệu cho cầu thủ
    values = df.loc[df['name'] == player, attributes].values.flatten()

    # Số lượng thuộc tính
    num_vars = len(attributes)

    # Tạo một bảng cho biểu đồ radar
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    values = np.concatenate((values, [values[0]]))
    angles += angles[:1]

    colors = ['b', 'r', 'g', 'm', 'y']

    ax.set_facecolor('#f0f0f0')

    # Vẽ biểu đồ radar với màu sắc cho từng thuộc tính
    for i in range(num_vars):
        ax.plot(angles[i:i + 2], values[i:i + 2], color=colors[i % len(colors)], linewidth=2)
        ax.fill(angles, values, facecolor=colors[i % len(colors)], alpha=0.25)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes)

    ax.set_title(f'Radar Chart for: {player}', weight='bold', size='medium', position=(0.5, 1.1),
                 horizontalalignment='center', verticalalignment='center')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Draw radar charts to compare players.")
    parser.add_argument('--file', type=str, default='E:/World/Code/Python/BTL/bai3/file/result.csv')
    args = parser.parse_args()

    # Đọc dữ liệu từ file
    df = pd.read_csv(args.file)

    # Lấy tên của hai cầu thủ từ hai dòng đầu tiên
    player1 = df['name'].iloc[0]
    player2 = df['name'].iloc[1]

    # Đặt thuộc tính mặc định để so sánh
    default_attributes = ['age', 'matches_played', 'PrgP', 'Pass_Cmp', 'Medium_Cmp', 'Pass_Live']

    # Tạo hình ảnh với hai biểu đồ radar
    fig, axs = plt.subplots(1, 2, figsize=(16, 8), subplot_kw=dict(polar=True))

    # Vẽ biểu đồ cho mỗi cầu thủ
    create_radar_chart(axs[0], player1, default_attributes)
    create_radar_chart(axs[1], player2, default_attributes)

    # Lưu hình ảnh vào tệp PNG
    plt.savefig('E:/World/Code/Python/BTL/bai3/file/radar_charts.png', bbox_inches='tight')
    plt.show()
