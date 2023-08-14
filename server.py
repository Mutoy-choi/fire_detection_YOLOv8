from ultralytics import YOLO
import torch
from PIL import Image
from bottle import Bottle, request, template, static_file
from io import BytesIO
import base64
from waitress import serve

app = Bottle()

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLO("runs/detect/train18/weights/best.pt")
model.to(device)

@app.route('/')
def index():
    return template('index.html')

@app.route('/predict', method=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files.get('file')
        img = Image.open(file.file)  # 원본 이미지

        # 이미지 전처리 및 모델에 입력
        results = model(img)

        # 예측 결과 이미지 생성
        for r in results:
            im_array = r.plot()  # plot a BGR numpy array of predictions
            predicted_img = Image.fromarray(im_array[..., ::-1])  # RGB PIL image

        # 이미지를 Base64로 인코딩
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        buffered_pred = BytesIO()
        predicted_img.save(buffered_pred, format="PNG")
        predicted_img_str = base64.b64encode(buffered_pred.getvalue()).decode()

        # Base64로 인코딩된 이미지를 HTML 페이지에 전달
        return template('index.html', original_img_data=img_str, predicted_img_data=predicted_img_str)
    else:
        return template('index.html')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=12321)

