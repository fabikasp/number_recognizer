from neural_network.neural_network import NeuralNetwork
import numpy


class NeuralNetworkFactory:
    @staticmethod
    def invoke_neural_network(include_testing: bool = False):
        amount_of_input_nodes = 28 * 28  # amount of pixels the images should have
        amount_of_hidden_nodes = 100
        amount_of_output_nodes = 10  # amount of possible numbers
        learning_rate = 0.3

        try:
            weights_input_hidden = numpy.load('./resources/weights_input_hidden.npy')  # load stored weights
        except Exception:
            weights_input_hidden = None

        try:
            weights_hidden_output = numpy.load('./resources/weights_hidden_output.npy')  # load stored weights
        except Exception:
            weights_hidden_output = None

        neural_network = NeuralNetwork(
            amount_of_input_nodes,
            amount_of_hidden_nodes,
            amount_of_output_nodes,
            learning_rate,
            weights_input_hidden,
            weights_hidden_output
        )

        if weights_input_hidden is None and weights_hidden_output is None:  # if no training took place in the past
            neural_network = NeuralNetworkFactory.__train_neural_network(neural_network)

            # store trained weights
            numpy.save('./resources/weights_input_hidden.npy', neural_network.get_weights_input_hidden())
            numpy.save('./resources/weights_hidden_output.npy', neural_network.get_weights_hidden_output())

        if include_testing:
            NeuralNetworkFactory.__test_neural_network(neural_network)

        return neural_network

    @staticmethod
    def __train_neural_network(neural_network: NeuralNetwork):
        training_data_file = open('resources/training_data.csv', 'r')
        training_records = training_data_file.readlines()
        training_data_file.close()

        for i in range(5):  # repeat training five times
            for training_record in training_records:
                image_values = training_record.split(',')

                #  bring image_values into intervals between 0.01 and 1
                input_values = (numpy.asfarray(image_values[1:]) / 255.0 * 0.99) + 0.01

                # all numbers get output value 0.01
                target_values = numpy.zeros(neural_network.get_output_nodes()) + 0.01
                target_values[int(image_values[0])] = 0.99  # recognized number gets output value 0.99

                neural_network.train(input_values, target_values)

        return neural_network

    @staticmethod
    def __test_neural_network(neural_network: NeuralNetwork):
        test_data_file = open('resources/test_data.csv', 'r')
        test_records = test_data_file.readlines()
        test_data_file.close()

        amount_of_outputs = 0
        amount_of_correct_outputs = 0
        for test_record in test_records:
            image_values = test_record.split(',')

            #  bring image_values into intervals between 0.01 and 1
            input_values = (numpy.asfarray(image_values[1:]) / 255.0 * 0.99) + 0.01

            output_values = neural_network.run(input_values)  # get outputs for inputs
            amount_of_outputs += 1

            correct_output = int(image_values[0])
            actual_output = numpy.argmax(output_values)

            if actual_output == correct_output:
                amount_of_correct_outputs += 1

        print("Accuracy = ", (amount_of_correct_outputs / amount_of_outputs) * 100, ' %')  # print accuracy
