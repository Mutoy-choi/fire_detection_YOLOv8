# fire_detection_YOLOv8

Yolov8을 사용한 fire detection

flask 라이브러리를 사용해서 server.py에 로컬 서비스를 구축했습니다.


## 코드 실행 환경 구성

코드를 실행하기 위해 다음 단계를 수행해야 합니다:

필요한 라이브러리(ultralytics, torch, PIL, flask, waitress)를 설치합니다.
해당 코드를 복사하여 파이썬 스크립트 파일로 저장합니다.
별도의 index.html 파일이 필요하므로 해당 파일도 생성합니다.
웹 서버 실행:

터미널을 열고 스크립트 파일이 있는 디렉토리로 이동합니다.

다음 명령을 사용하여 웹 서버를 실행합니다:

python server.py

## 웹 페이지 접속

웹 서버가 실행되고 있으면, 브라우저에서 다음 주소로 접속합니다: http://localhost:12321

## 웹 페이지 사용

웹 페이지에 접속하면 이미지를 업로드할 수 있는 간단한 화면이 표시됩니다.
"Choose File" 버튼을 클릭하여 컴퓨터에서 이미지 파일을 선택합니다.
이미지를 선택한 후 "Predict" 버튼을 클릭합니다.
서버는 이미지를 처리하고, 원본 이미지와 객체 검출 결과를 함께 시각화하여 보여줍니다.

예시
![example](https://github.com/Mutoy-choi/fire_detection_YOLOv8/assets/87027571/e82135d7-314b-4750-84d3-16b0e1f628ae)


## 웹 사이트 종료

웹 페이지를 확인한 후 원하는 경우 터미널에서 Ctrl+C를 눌러 웹 서버를 종료할 수 있습니다.

https://drive.google.com/file/d/1Q9E67OtuaZIKlYsaG2VZb2cNES-73O1O/view?usp=drive_link
best.pt 링크입니다.
