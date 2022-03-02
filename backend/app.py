from flask import Flask, jsonify, request
from PIL import Image
from neural_network.neural_network_factory import NeuralNetworkFactory
import base64
import io
import numpy

app = Flask(__name__)


@app.post('/')
def evaluate_number_in_picture():
    encoded_image_bytes = request.values['encodedImageBytes'] if 'encodedImageBytes' in request.values else None

    if encoded_image_bytes is not None:
        image = Image.open(io.BytesIO(base64.b64decode(encoded_image_bytes)))
        image = image.resize((28, 28), Image.ANTIALIAS)

        rgba_values = list(image.getdata())
        pixel_values = []
        for rgba_value in rgba_values:
            red = rgba_value[0] & 0xFF
            green = rgba_value[1] & 0xFF
            blue = rgba_value[2] & 0xFF
            alpha = rgba_value[3] & 0xFF

            pixel_values.append((red << 24) + (green << 16) + (blue << 8) + alpha)  # transform rgba values to one value

        input_values = (numpy.asfarray(pixel_values) / 255.0 * 0.99) + 0.01
        result_number = numpy.argmax(neural_network.run(input_values))

        response = {'resultNumber': int(result_number)}
    else:
        response = {'resultNumber': None}

    return jsonify(response)


if __name__ == '__main__':
    neural_network = NeuralNetworkFactory.invoke_neural_network()

    app.run()
