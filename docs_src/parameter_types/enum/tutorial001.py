from enum import Enum

import doctyper


class NeuralNetwork(str, Enum):
    simple = "simple"
    conv = "conv"
    lstm = "lstm"


def main(network: NeuralNetwork = NeuralNetwork.simple):
    print(f"Training neural network of type: {network.value}")


if __name__ == "__main__":
    doctyper.run(main)
