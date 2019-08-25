from flask import Flask

# prediction means inference.

# keras is the deep learning library
from keras.models import load_model

# keras trained model on a lot of images
from keras.applications.resnet50 import ResNet50

app = Flask(__name__)

MODEL_PATH = 'models/my_model.h5'
model = ResNet50(weights='imagenet')

def model_predict(img_path, model):
    img = image.load_image(img_path)
    x = image.img_to_array(img)
    preds = models.predict(x)
    return preds

@app.route('/')
def index():
    return render_template('index.html')

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
