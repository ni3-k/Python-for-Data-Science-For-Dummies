from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

# Loading the Data
boston = load_boston()
X, y = boston.data, boston.target

# Training a Model
hypothesis = LinearRegression(normalize = True)
hypothesis.fit(X, y)

# Viewing a Result
print(hypothesis.coef_)