from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os
from keras.models import load_model

try:
    import shutil
    shutil.rmtree('uploads/image')
    os.chdir('uploads')
    os.mkdir('image')
    os.chdir('..')
    print()
except:
    pass

MODEL_PATH = 'assets/multiclassgarbage.h5'
model = load_model(MODEL_PATH)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/image'

@app.route('/')
def upload_f():
    return render_template('upload.html')

def finds():
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    vals = ['Looks like CARDBOARD', 'GLASS', 'METAL', 'THATS PAPER', 'HAZARDOUS PLASTIC', 'TRASH']
    test_dir = 'uploads'
    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(200, 200),
        color_mode="rgb",
        shuffle=False,
        class_mode='categorical',
        batch_size=1)

    pred = model.predict_generator(test_generator)
    print(pred)
    return str(vals[np.argmax(pred)])

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        val = finds()
        return render_template('pred.html', ss=val)

if __name__ == '__main__':
    app.run()
