from flask import Flask
from flask import render_template
# prediction means inference.
import os
import numpy as np

from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input, decode_predictions

# keras is the deep learning library
from keras.models import load_model

# keras trained model on a lot of images
from keras.applications.resnet50 import ResNet50

app = Flask(__name__)

MODEL_PATH = 'models/my_model.h5'
model = ResNet50(weights='imagenet')
model._make_predict_function()

def model_predict(img_path='./tree.jpg', model=model):
    from datetime import datetime
    start = datetime.now()
    assert os.path.isfile(img_path), f'missing file {img_path}'
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    print(decode_predictions(preds, top=10))
    print("DURATION:", (datetime.now()-start).total_seconds())
    return preds

@app.route('/')
def index():
    print("model prediction", model_predict())
    return render_template('./index.html')

@app.route('/predict')
def upload():
    """Sending an image to the server
    """
    if request.method == 'POST':
        f = request.files['file']
        f.save(file_path)
        preds = model_predict(file_path, model)
        pred_class = decode_predictions(preds, top=1)
        return pred_class

# run with flask run.
