
# ❤️ Heart Disease Prediction Using Machine Learning

## 📌 Project Overview

This project uses Machine Learning to predict whether a person may have heart disease based on health-related parameters. It uses Python, Pandas, NumPy, Scikit-learn, Matplotlib, and Seaborn to process data, train a Decision Tree model, and generate predictions.

The project includes data preprocessing, outlier removal, feature scaling, model training, model evaluation, and user input for individual predictions.

## 🎯 Objectives

- Analyze heart disease data using Python.
- Remove outliers using the Interquartile Range (IQR) method.
- Preprocess and standardize numerical features.
- Train a Decision Tree model using Scikit-learn.
- Evaluate model performance on test data.
- Predict heart disease status using user-provided health parameters.

## 🛠️ Technologies Used

- **Python** — Programming language
- **NumPy** — Numerical operations
- **Pandas** — Data manipulation and analysis
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical data visualization
- **Scikit-learn** — Machine Learning and model evaluation

## 📂 Project Structure

```text
Heart-Disease-Prediction/
│
├── heart.csv          # Heart disease dataset
├── main.py            # Main Python program
├── README.md          # Project documentation
└── requirements.txt   # Required Python packages
```

## 📊 Dataset

The project uses a dataset named `heart.csv`.

The dataset is expected to contain health-related features such as:

| Feature | Description |
|---|---|
| `age` | Age of the patient |
| `sex` | Sex category |
| `cp` | Chest pain type |
| `trestbps` | Resting blood pressure |
| `chol` | Serum cholesterol |
| `fbs` | Fasting blood sugar indicator |
| `restecg` | Resting electrocardiographic results |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise-induced angina |
| `oldpeak` | ST depression induced by exercise |
| `slope` | Slope of the peak exercise ST segment |
| `ca` | Number of major vessels |
| `thal` | Thalassemia-related category |
| `target` | Heart disease outcome label |

**Note:** The dataset must contain the expected feature columns and a `target` column. Actual category values and target-label meanings depend on the dataset version.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Heart-Disease-Prediction.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Navigate to the project directory

```bash
cd Heart-Disease-Prediction
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

Alternatively, install the dependencies directly:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

## ▶️ How to Run

Make sure that `heart.csv` is located in the project directory.

Run the Python program:

```bash
python main.py
```

The program will:

1. Load the heart disease dataset.
2. Remove outliers using the IQR method.
3. Separate the input features and target variable.
4. Split the data into training and testing sets.
5. Standardize the features using `StandardScaler`.
6. Train a Decision Tree model.
7. Evaluate the model on the test dataset.
8. Ask the user to enter health-related parameters.
9. Display the predicted heart disease status and evaluation score.

## 🧠 Machine Learning Workflow

```text
Heart Disease Dataset
          |
          v
    Data Loading
          |
          v
   Outlier Removal
          |
          v
 Feature Selection
          |
          v
 Train-Test Split
          |
          v
  Feature Scaling
          |
          v
 Decision Tree Model
          |
          v
 Model Evaluation
          |
          v
   User Input Data
          |
          v
 Heart Disease Prediction
```

## 📈 Model Evaluation

The project imports the following evaluation metrics from Scikit-learn:

- **Accuracy:** Measures the proportion of correct predictions.
- **Precision:** Measures how many positive predictions are correct.
- **Recall:** Measures how many actual positive cases are identified.
- **Confusion Matrix:** Summarizes correct and incorrect classifications.

The current implementation calculates accuracy only. Precision, recall, and the confusion matrix can be added for more detailed evaluation.

## 📦 Requirements

Create a file named `requirements.txt` with the following content:
numpy
pandas
matplotlib
seaborn
scikit-learn


## 🚀 Future Improvements

- Use `DecisionTreeClassifier` for the binary classification task.
- Correct the input data types and validate user inputs.
- Display precision, recall, F1-score, and a confusion matrix.
- Add exploratory data analysis and visualizations.
- Improve outlier handling and missing-value treatment.
- Build a web interface using Streamlit or Flask.
- Compare multiple classification algorithms.
- Save and load the trained model and scaler.

## ⚠️ Important Notes

- This project is intended for educational and research purposes.
- The predictions are not medical diagnoses and must not replace professional medical advice.
- Model performance depends on dataset quality, preprocessing, and the selected algorithm.
- The reported accuracy is a test-set evaluation score, not a confidence score for an individual prediction.

## 👨‍💻 Author

**Your Name**

- GitHub: [Your GitHub Profile](https://github.com/YOUR-USERNAME)

## 📄 License

This project is available for educational use. Add a `LICENSE` file if you want to specify the terms under which others may use, modify, or distribute your code.
