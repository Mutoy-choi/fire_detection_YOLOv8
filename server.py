from ultralytics import YOLO
import torch
from PIL import Image
from flask import Flask, request, render_template, send_from_directory
from io import BytesIO
import base64

app = Flask(__name__, template_folder='templates', static_folder='static')

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLO("runs/detect/train18/weights/best.pt")
model.to(device)

@app.route('/')
def index():
    return render_template('index.html', original_img_data="", predicted_img_data="")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img = Image.open(file.stream)  # 원본 이미지

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
        return render_template('index.html', original_img_data=img_str, predicted_img_data=predicted_img_str)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12321, debug=True)

