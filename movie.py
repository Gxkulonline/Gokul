import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Assuming you have a dataset with features like genre, director, actors, etc., along with the movie ratings
# Load your dataset
movie_data = pd.read_csv("IMDb Movies India.csv")  # Replace "movie_data.csv" with your dataset file path

# Assuming you have already preprocessed your data and encoded categorical variables

# Selecting relevant features
features = ['genre', 'director', 'actor1', 'actor2', 'actor3']

# Splitting the dataset into training and testing sets
X = movie_data[features]
y = movie_data['rating']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing and training the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting movie ratings on the test set
predictions = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)
