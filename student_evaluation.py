import pandas as pd

# Hàm tính điểm trung bình môn học
def calculate_subject_average(hk1, hk2):
    return round((hk1 + hk2 * 2) / 3, 1)

# Hàm đánh giá học sinh
def evaluate_student(averages):
    try:
        if averages['GPA'] >= 8.0 and all(averages[subject] >= 6.5 for subject in averages if subject != 'GPA') and (averages['Toán'] >= 8.0 or averages['Văn'] >= 8.0):
            return 'Giỏi'
        elif averages['GPA'] >= 6.5 and all(averages[subject] >= 5.0 for subject in averages if subject != 'GPA') and (averages['Toán'] >= 6.5 or averages['Văn'] >= 6.5):
            return 'Khá'
        elif averages['GPA'] >= 5.0 and all(averages[subject] >= 3.5 for subject in averages if subject != 'GPA') and (averages['Toán'] >= 5.0 or averages['Văn'] >= 5.0):
            return 'Trung bình'
        else:
            return 'Yếu'
    except KeyError as e:
        print(f"Lỗi KeyError: {e} - Có thể tên môn học bị sai hoặc không tồn tại trong dữ liệu.")
        print("Các môn học hiện có:", averages.keys())
        raise

# Hàm xử lý từng học sinh và lưu kết quả vào file Excel
def count_evaluate_students(file_path):
    df = pd.read_excel(file_path, header=None)
    
    # Khởi tạo DataFrame kết quả với cột Tên 
    grade_counts_by_year = {
        'Lớp 10': {'Giỏi': 0, 'Khá': 0, 'Trung bình': 0, 'Yếu': 0},
        'Lớp 11': {'Giỏi': 0, 'Khá': 0, 'Trung bình': 0, 'Yếu': 0},
        'Lớp 12': {'Giỏi': 0, 'Khá': 0, 'Trung bình': 0, 'Yếu': 0},
        'Cả 3 năm': {'Giỏi': 0, 'Khá': 0, 'Trung bình': 0, 'Yếu': 0}
    }

    for index, row in df.iterrows():
        student_name = row[0]
        student_result = {'Tên': student_name}

        for year in range(1, 4):
            start_col = (year - 1) * 18 + 1
            end_col = start_col + 18
            year_columns = row[start_col:end_col]

            # Tính điểm trung bình các môn học
            subject_averages = {
                'Toán': calculate_subject_average(year_columns.iloc[0], year_columns.iloc[9]),
                'Văn': calculate_subject_average(year_columns.iloc[1], year_columns.iloc[10]),
                'Lý': calculate_subject_average(year_columns.iloc[2], year_columns.iloc[11]),
                'Hóa': calculate_subject_average(year_columns.iloc[3], year_columns.iloc[12]),
                'Sinh': calculate_subject_average(year_columns.iloc[4], year_columns.iloc[13]),
                'Sử': calculate_subject_average(year_columns.iloc[5], year_columns.iloc[14]),
                'Địa': calculate_subject_average(year_columns.iloc[6], year_columns.iloc[15]),
                'GDCD': calculate_subject_average(year_columns.iloc[7], year_columns.iloc[16]),
                'Anh': calculate_subject_average(year_columns.iloc[8], year_columns.iloc[17])
            }

            # Tính GPA
            subject_averages['GPA'] = pd.Series(subject_averages).mean()

            # Đánh giá học sinh
            grade = evaluate_student(subject_averages)

            if year == 1:
                grade_counts_by_year['Lớp 10'][grade] += 1
            elif year == 2:
                grade_counts_by_year['Lớp 11'][grade] += 1
            elif year == 3:
                grade_counts_by_year['Lớp 12'][grade] += 1
            grade_counts_by_year['Cả 3 năm'][grade] +=1

       
        

        # Đếm loại xếp loại nhiều nhất cho cả 3 năm và cập nhật vào "Cả 3 năm"
        

    print(grade_counts_by_year)
    return 

# Đường dẫn tới file Excel
file_path = "E:/Download/ScorePredict/data/TN_TN.xlsx"
output_file = "E:/Download/ScorePredict/data/TN_TN_student_evaluation.xlsx"

# Chạy hàm để đánh giá học sinh
count_evaluate_students(file_path)
