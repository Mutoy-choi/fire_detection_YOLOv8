from ultralytics import YOLO
import torch
from PIL import Image

# GPU 활성화
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)

# Load a model
model = YOLO("yolov8m.yaml")  # build a new model from scratch
model = YOLO("runs/detect/train18/weights/best.pt")  # load a pretrained model (recommended for training)

results = model('optimize.jpg')

# Show the results
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save('results.jpg')  # save image