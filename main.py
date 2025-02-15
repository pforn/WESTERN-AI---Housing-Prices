"""
Psuedo code:

"""


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn import tree



TEST_SIZE = 0.2

def load_data(filename):
    data = pd.read_csv(filename)
    sale_price = data['SalePrice']
    evidence = data.drop('SalePrice', 1)


    enc = LabelEncoder()

    # convert non-numeric evidence to numeric
    for col in evidence:
        for i in range(len(evidence[col])):
            if isinstance(evidence[col][i], str) and evidence[col][i] != 'NA':
                enc.fit(evidence[col])
                evidence[col] = enc.transform(evidence[col])
                break

    evidence = evidence.fillna(0)  # get rid of any null values


    return evidence, sale_price


def train_model(evidence, labels):
    model = LinearRegression().fit(evidence, labels)
    #model = tree.DecisionTreeRegressor().fit(evidence, labels)
    return model

def test_model(labels, predictions):
    count = 0
    for actual in labels:
        print("Prediction: ", predictions[count], " ---- actual: ", actual)
        count += 1
        if count > 10:
            break

    print("----------------------------------------------")
    print("R squared value: ", model.score(X_test, y_test))
    print("Number of feature: ", X_train.shape[1])



file = 'train.csv'

# Load data from spreadsheet and split into train and test set

evidence, labels = load_data(file)
X_train, X_test, y_train, y_test = train_test_split(
    evidence, labels, test_size=TEST_SIZE
)

# Train model and make predictions
model = train_model(X_train, y_train)
predictions = model.predict(X_test)
test_model(y_test, predictions)


