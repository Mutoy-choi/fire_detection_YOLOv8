import os
import random

# 데이터 폴더 경로 설정
data_path = '/home/fire/dataset/test/images'  # 여기에 이미지 폴더의 경로를 입력하세요.
all_files = [f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, f)) and f.endswith('.jpg')]  # .jpg 이미지만 대상으로 함

# 파일 경로 저장
with open('/home/fire/test.txt', 'w') as f:
    for file in all_files:
        f.write(os.path.join(data_path, file) + '\n')
