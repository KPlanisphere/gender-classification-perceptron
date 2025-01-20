# Gender Classification Perceptron

This repository contains a simple perceptron-based model that classifies a person's gender based on height, weight, testosterone levels, and estrogen levels. The model is trained using a dataset stored in `sex.txt`.

<p align= "center">
    <img src="https://github.com/user-attachments/assets/15bd32c6-6dbb-4fba-8e89-b56a12031ebd" style="width: 50%; height: auto;">
</p>

## 📌 Overview

The perceptron algorithm is used to classify individuals into two categories:
- **0 → Male**
- **1 → Female**

The model takes the following features as input:
- Height (cm)
- Weight (kg)
- Testosterone levels (ng/dL)
- Estrogen levels (pg/mL)

## 🚀 Requirements

To run this project, you need:

- Python 3.x
- Required libraries:
```bash
  pip install matplotlib
```

## 🔧 Usage

### 1️⃣ Prepare the Dataset

Ensure the file `sex.txt` is in the same directory. The dataset should follow this format:

```arduino
height,weight,sex,testosterone,estrogen;
```

Example:

```170,56,1,52.27,259.17;
172,63,0,909.52,18.17;
```

-   **1** → Female
-   **0** → Male

### 2️⃣ Train the Model

Run the script:

```bash
python perceptron.py
```

The program will train a perceptron with 10,000 iterations using the dataset.

### 3️⃣ Make Predictions

After training, the program prompts the user for:

-   Height (cm)
-   Weight (kg)
-   Testosterone levels (ng/dL)
-   Estrogen levels (pg/mL)

Then, the perceptron predicts and outputs:

```diff
-> FEMALE
```

or

```diff
-> MALE
```

### 4️⃣ Error Plot

At the end of execution, the program generates a plot displaying training errors over time.

<p align= "center">
    <img src="https://github.com/user-attachments/assets/d7713daf-2f66-4c38-86ef-584328d72aa3" style="width: 50%; height: auto;">
</p>
