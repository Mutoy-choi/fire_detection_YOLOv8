import os
import random

# 데이터 폴더 경로 설정
data_path = '/home/fire/dataset/train/images'  # 여기에 이미지 폴더의 경로를 입력하세요.
all_files = [f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, f)) and f.endswith('.jpg')]  # .jpg 이미지만 대상으로 함

# 데이터 섞기
random.shuffle(all_files)

# 학습 및 검증 데이터셋으로 분할 (예: 80%는 학습, 20%는 검증용으로 사용)
split_ratio = 0.8
split_idx = int(len(all_files) * split_ratio)
train_files = all_files[:split_idx]
valid_files = all_files[split_idx:]

# 파일 경로 저장
with open('/home/fire/train.txt', 'w') as f:
    for file in train_files:
        f.write(os.path.join(data_path, file) + '\n')

with open('/home/fire/valid.txt', 'w') as f:
    for file in valid_files:
        f.write(os.path.join(data_path, file) + '\n')
