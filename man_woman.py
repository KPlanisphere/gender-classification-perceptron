import random
import matplotlib.pyplot as plt
import sys

class Perceptron:
    def __init__(self, input_number, step_size=0.1):
        self._ins = input_number
        self._w = [random.random() for _ in range(input_number)]
        self._eta = step_size
        
    def predict(self, inputs):
        weighted_average = sum(w * elm for w, elm in zip(self._w, inputs))
        return 1 if weighted_average > 0 else 0

    def train(self, inputs, ex_output):
        output = self.predict(inputs)
        error = ex_output - output
        if error != 0:
            self._w = [w + self._eta * error * x for w, x in zip(self._w, inputs)]
        return error


# Read input data from 'sex.txt'
def load_data_from_file(file_name):
    input_data = []
    with open(file_name, 'r') as file:
        for line in file:
            if line.strip():  # Ensure there's no empty line
                parts = line.strip().strip(';').split(',')
                altura = float(parts[0])
                peso = float(parts[1])
                sexo = int(parts[2])
                testosterona = float(parts[3])
                estrogeno = float(parts[4])
                input_data.append([altura, peso, testosterona, estrogeno, sexo])
    return input_data

# File path to the data
file_name = 'sex.txt'
input_data = load_data_from_file(file_name)

# Initialize Perceptron with 4 inputs (height, weight, testosterone, estrogen)
pr = Perceptron(5, 0.1)  # Perceptron with 5 inputs
weights = []  # List to store weights
errors = []   # List to store errors

# Training phase
for _ in range(10000):
    for person in input_data:
        output = person[-1]  # Last value is the expected output (sex)
        inp = [1] + person[0:-1]  # Add bias term (1) to the input
        weights.append(pr._w)
        err = pr.train(inp, output)
        errors.append(err)

# User input for testing
h = float(input("\nIntroduce tu estatura en centímetros:  "))
w = float(input("Introduce tu peso en kilogramos:  "))

# Testosterone and estrogen levels

print("\n\tTESTOSTERONA (ng/dL)")
print("\t| Hombres: 300 a 1,000 ng/dL")
print("\t| Mujeres: 15 a 70 ng/dL")

print("\n\tESTRÓGENO (pg/mL)")
print("\t| Hombres: 10 a 50 pg/mL")
print("\t| Mujeres: 50 a 300 pg/mL\n")

t = float(input("Introduce tus niveles de testosterona en ng/dL:  "))
e = float(input("Introduce tus niveles de estrógeno en pg/mL:  "))

# Prediction based on user inputs
if pr.predict([1, h, w, t, e]) == 1:
    print("\n\t-> MUJER\n")
else:
    print("\n\t-> HOMBRE\n")

# Plot errors
plt.plot(errors)
plt.show()
