# import numpy as np
# import pandas as pd

# def calculate_correlations_10_11_12():
#     file = "E:\Download\ScorePredict\data\10_11_12.xlxs"
#     df = pd.DataFrame(pd.read_excel(file, header=None, sheet_name='10_11_12', names=names)).drop(columns='Name', axis=1)
#     print(df)
#     correlations = np.corrcoef(df, rowvar=False)
#     return correlations


# def calculate_correlations_TN(data_file):
#     file = data_file
#     df = pd.DataFrame(pd.read_excel(file, header=None, sheet_name='10_11_12', names=names)).drop(columns='Name', axis=1)
#     print(df)
#     correlations = np.corrcoef(df, rowvar=False)
#     return correlations

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu từ file .xlsx
file_path = "E:/Download/ScorePredict/data/10_11_12_LR_test_predict.xlsx"
df = pd.read_excel(file_path)

# Tạo hàm tính số lượng điểm trong các khoảng 0.5
def calculate_bins(data, bin_size=0.5):
    bins = np.arange(0, 10.5, bin_size)  # Tạo các khoảng từ 0 đến 10 với khoảng cách 0.5
    bin_counts = pd.cut(data, bins=bins, include_lowest=True).value_counts().sort_index()
    return bin_counts

# Các môn học cần vẽ biểu đồ
subjects = ['Maths', 'Literature', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'English', 'Civic Education']

# Vẽ biểu đồ đường cho từng môn học
for subject in subjects:
    actual_col = f"{subject}_1_12"
    pred_col = f"{subject}_1_12_pred"

    actual_counts = calculate_bins(df[actual_col])
    pred_counts = calculate_bins(df[pred_col])

    plt.figure(figsize=(10, 6))
    plt.plot(actual_counts.index.astype(str), actual_counts.values, label='Actual', marker='o')
    plt.plot(pred_counts.index.astype(str), pred_counts.values, label='Predicted', marker='o')
    
    plt.title(f'{subject} - Comparison of Actual and Predicted Scores')
    plt.xlabel('Score Range')
    plt.ylabel('Count')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
