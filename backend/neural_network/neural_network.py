from scipy.special import expit
import numpy


class NeuralNetwork:
    def __init__(
        self,
        amount_of_input_nodes,
        amount_of_hidden_nodes,
        amount_of_output_nodes,
        learning_rate,
        weights_input_hidden,  # can be None
        weights_hidden_output  # can be None
    ):
        self.__amount_of_input_nodes = amount_of_input_nodes
        self.__amount_of_hidden_nodes = amount_of_hidden_nodes
        self.__amount_of_output_nodes = amount_of_output_nodes
        self.__learning_rate = learning_rate

        self.__weights_input_hidden = (numpy.random.rand(self.__amount_of_hidden_nodes, self.__amount_of_input_nodes) - 0.5) \
            if weights_input_hidden is None \
            else weights_input_hidden
        self.__weights_hidden_output = (numpy.random.rand(self.__amount_of_output_nodes, self.__amount_of_hidden_nodes) - 0.5) \
            if weights_hidden_output is None \
            else weights_hidden_output

    def __activate_node(self, weighted_input_values):
        return expit(weighted_input_values)

    def train(self, input_values, target_values):
        input_array = numpy.array(input_values, ndmin=2).T
        target_array = numpy.array(target_values, ndmin=2).T

        inputs_hidden = numpy.dot(self.__weights_input_hidden, input_array)  # calc weighted inputs for hidden layer
        outputs_hidden = self.__activate_node(inputs_hidden)  # sigmoid function to sum up the inputs

        inputs_output = numpy.dot(self.__weights_hidden_output, outputs_hidden)  # calc weighted inputs for output layer
        outputs_output = self.__activate_node(inputs_output)  # sigmoid function to sum up the inputs

        output_errors = target_array - outputs_output  # calc difference between expected and actual output values

        hidden_errors = numpy.dot(
            self.__weights_hidden_output.T,
            output_errors
        )  # lead back output errors to hidden errors

        self.__weights_hidden_output += self.__learning_rate * numpy.dot(
            (output_errors * outputs_output * (1.0 - outputs_output)),
            numpy.transpose(outputs_hidden)
        )  # manipulate hidden_output weights depending on the output errors

        self.__weights_input_hidden += self.__learning_rate * numpy.dot(
            (hidden_errors * outputs_hidden * (1.0 - outputs_hidden)),
            numpy.transpose(input_array)
        )  # manipulate input_hidden weights depending on the hidden errors

    def run(self, input_values):
        input_array = numpy.array(input_values, ndmin=2).T

        inputs_hidden = numpy.dot(self.__weights_input_hidden, input_array)
        outputs_hidden = self.__activate_node(inputs_hidden)

        inputs_output = numpy.dot(self.__weights_hidden_output, outputs_hidden)
        outputs_output = self.__activate_node(inputs_output)

        return outputs_output

    def get_input_nodes(self):
        return self.__amount_of_input_nodes

    def get_hidden_nodes(self):
        return self.__amount_of_hidden_nodes

    def get_output_nodes(self):
        return self.__amount_of_output_nodes

    def get_learning_rate(self):
        return self.__learning_rate

    def get_weights_input_hidden(self):
        return self.__weights_input_hidden

    def get_weights_hidden_output(self):
        return self.__weights_hidden_output
