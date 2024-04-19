import pandas as pd
from scipy.stats import shapiro

# 入力と出力のファイルパス
input_csv_path = 'BarGraph_correlation_coefficient_for_trial-to-trial_comparison.csv'
output_csv_path = 'shapiro_results.csv'

# CSVファイル読み込み
data = pd.read_csv(input_csv_path)

# 結果を格納するリストの初期化
results = []

# 各列に対してシャピロ–ウィルク検定を実行
for column in data.columns:
    stat, p_value = shapiro(data[column])
    
    # 棄却されるかどうかの判定
    rejected = 'Yes' if p_value < 0.05 else 'No'
    
    # 結果をリストに追加
    results.append([column, stat, p_value, rejected])

# 結果をデータフレームに変換
results_df = pd.DataFrame(results, columns=['Column', 'Stat', 'P-value', 'Rejected'])

# 結果をCSVファイルに保存
results_df.to_csv(output_csv_path, index=False)

print("シャピロ–ウィルク検定の結果が '{}' に保存されました。".format(output_csv_path))






