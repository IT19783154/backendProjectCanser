import logging
import numpy as np
from PIL import Image, ImageOps
import tensorflow as tf
from keras.models import load_model
import operator
tf.get_logger().setLevel(logging.ERROR)


def MLPredict(image):
    # Load the model
    model = load_model('detectot\TF_model.h5')
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    size = (224, 224)

    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)

    prediction = prediction.tolist()
    # print(model.summary())

    prediction = prediction[0]

    predictionresult = []

    for x in prediction:
        predictionresult.append(round((x*100), 1))

    if max(predictionresult) > 90:  # flase positve patch
        result = {
            "melanoma": predictionresult[0],
            "normal Skin": predictionresult[1],
        }

        Result = max(result.items(), key=operator.itemgetter(1))[0]

        print("ML funcation is Working....")
        print(Result)
        return Result

    else:
        print("ML funcation is Working....")
        return "Error"
