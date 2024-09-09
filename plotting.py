import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


# Dữ liệu độ chính xác của 3 mô hình cho từng môn học lớp 12 (2 học kỳ)
subjects = [
    "Maths_1_12", "Literature_1_12", "Physics_1_12", "Chemistry_1_12", "Biology_1_12",
    "History_1_12", "Geography_1_12", "English_1_12", "Civic Education_1_12",
    "Maths_2_12", "Literature_2_12", "Physics_2_12", "Chemistry_2_12", "Biology_2_12",
    "History_2_12", "Geography_2_12", "English_2_12", "Civic Education_2_12"
]

accuracy_linear_regression = [
    90.504289, 93.332013, 88.809074, 91.844177, 89.797066, 91.467157, 90.575390,
    90.675338, 94.018301, 93.254125, 93.287290, 89.663183, 93.634354, 91.015423,
    92.729919, 93.381346, 90.752449, 95.753678
]

accuracy_mlp = [
    90.764183, 92.953630, 89.322169, 91.428534, 90.441082, 92.152978, 90.796356,
    90.409442, 93.986225, 92.550644, 93.078674, 88.823366, 93.540724, 91.123153,
    92.685804, 93.201315, 91.538729, 95.742400
]

accuracy_lstm = [
    90.636056, 93.033466, 88.865820, 91.533245, 90.309245, 91.370080, 91.044108,
    90.192758, 94.102417, 93.092102, 93.097026, 90.204119, 93.634972, 90.770257,
    92.775147, 93.150107, 91.107622, 95.835315
]

# Vẽ biểu đồ cột cho cả 3 mô hình
fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.2
index = np.arange(len(subjects))

bars1 = ax.bar(index, accuracy_linear_regression, bar_width, label="Linear Regression")
bars2 = ax.bar(index + bar_width, accuracy_mlp, bar_width, label="MLP")
bars3 = ax.bar(index + 2 * bar_width, accuracy_lstm, bar_width, label="LSTM")

ax.set_xlabel('Subjects')
ax.set_ylabel('Accuracy')
ax.set_title('Accuracy by Subject and Model')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(subjects, rotation=90)
ax.legend()

plt.tight_layout()
plt.savefig(f'static/Images/2.png')
plt.close()

# Vẽ biểu đồ cột riêng cho từng mô hình
def plot_individual_model_accuracy(model_name, accuracies):
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.bar(subjects, accuracies, color='blue', alpha=0.7)
    ax.set_xlabel('Subjects')
    ax.set_ylabel('Accuracy')
    ax.set_title(f'{model_name} - Accuracy by Subject')
    ax.set_xticklabels(subjects, rotation=90)
    plt.tight_layout()
    plt.savefig(f'static/Images/1.png')
    plt.show()

# Vẽ riêng cho từng mô hình
plot_individual_model_accuracy('Linear Regression', accuracy_linear_regression)
#plot_individual_model_accuracy('MLP', accuracy_mlp)
#plot_individual_model_accuracy('LSTM', accuracy_lstm)



def load_and_plot(file_path):
    # Load the Excel file
    df = pd.read_excel(file_path)

    # Define the subjects (actual and predicted)
    subjects = [
        "Maths_1_12", "Literature_1_12", "Physics_1_12", "Chemistry_1_12", "Biology_1_12",
        "History_1_12", "Geography_1_12", "English_1_12", "Civic Education_1_12",
        "Maths_2_12", "Literature_2_12", "Physics_2_12", "Chemistry_2_12", "Biology_2_12",
        "History_2_12", "Geography_2_12", "English_2_12", "Civic Education_2_12"
    ]

    # Create the bins for the intervals
    bins = np.arange(0, 10.5, 0.5)

    for subject in subjects:
        actual = df[subject]
        predicted = df[f'{subject}_pred']

        # Calculate histogram
        actual_hist, _ = np.histogram(actual, bins=bins)
        predicted_hist, _ = np.histogram(predicted, bins=bins)

        # Plot the results
        plt.figure(figsize=(10, 6))
        plt.plot(bins[:-1], actual_hist, label=f'Actual {subject}', marker='o')
        plt.plot(bins[:-1], predicted_hist, label=f'Predicted {subject}', marker='o', linestyle='--')
        plt.xlabel('Score Ranges')
        plt.ylabel('Number of Scores')
        plt.title(f'Distribution of Scores for {subject}')
        plt.legend()
        plt.grid(True)
        #plt.savefig(f'static/Images/{subject}.png')
        plt.show()


# file_path = "E:/Download/ScorePredict/data/10_11_12_LR_test_predict.xlsx"
# load_and_plot(file_path)

def calculate_correlations_TN(file_path):
    # Đọc file Excel
    df = pd.read_excel(file_path)
    # Bỏ cột 'Name'
    df = df.drop(columns=['Name'])
    correlation_matrix = df.corr()
    # Plot the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='Blues', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.savefig(f'static/Images/3.png')
    plt.show()


def plot_relationship_from_excel(file_path):
    # Đọc dữ liệu từ file Excel
    df = pd.read_excel(file_path, header=None)

    # Loại bỏ cột đầu tiên (cột tên)
    df = df.iloc[:, 1:]

    # Chia dữ liệu thành X (4 học kỳ đầu) và Y (2 học kỳ cuối)
    X = df.iloc[:, :36]  # 36 cột đầu
    Y = df.iloc[:, 36:]  # 18 cột cuối

    # Danh sách tên các môn học (tùy chỉnh theo dữ liệu của bạn)
    subjects = ['Maths', 'Literature', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'English', 'Civic Education']

    # Lặp qua tất cả các môn học và vẽ biểu đồ
    for i in range(9):  # 9 môn học
        plt.figure(figsize=(10, 6))
        plt.scatter(X.iloc[:, i], Y.iloc[:, i])
        plt.xlabel(f'{subjects[i]} (4 Học kỳ đầu)')
        plt.ylabel(f'{subjects[i]} (2 Học kỳ cuối)')
        plt.title(f'Mối quan hệ giữa {subjects[i]} (4 học kỳ đầu) và {subjects[i]} (2 học kỳ cuối)')
        plt.xlim(0, 10)
        plt.ylim(0, 10)
        plt.show()

# Gọi hàm với đường dẫn tới file Excel
plot_relationship_from_excel('E:/Download/ScorePredict/data/10_11_12.xlsx')

def plot_pie_chart(input_file):
    # Đọc dữ liệu từ file Excel
    df = pd.read_excel(input_file)
    
    # Tính điểm trung bình của 4 kỳ đầu tiên
    df['Average_4_terms'] = df.iloc[:, 1:37].mean(axis=1) # Lấy cột từ 1 đến 36
    
    # Phân loại vào các khoảng điểm
    bins = [0, 4.9, 6.4, 7.9, 10]
    labels = ['0-4.9', '5-6.4', '6.5-7.9', '8-10']
    df['Score_Range'] = pd.cut(df['Average_4_terms'], bins=bins, labels=labels, right=False)
    
    # Đếm số lượng học sinh trong mỗi khoảng
    score_counts = df['Score_Range'].value_counts(sort=False)
    
    # Vẽ biểu đồ tròn
    plt.figure(figsize=(8, 8))
    plt.pie(score_counts, labels=score_counts.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    plt.title('Biểu đồ phân bố điểm trung bình của học sinh')
    plt.show()

# Gọi hàm với đường dẫn đến file Excel
plot_pie_chart('E:/Download/ScorePredict/data/10_11_12.xlsx')