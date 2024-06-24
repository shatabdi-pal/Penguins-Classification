import pandas as pd
import numpy as np
import flask

penguins_df = pd.read_csv("penguins.csv")
penguins_df.dropna(inplace=True)


# Convert categorical features to numeric
penguins_df['sex'] = penguins_df['sex'].map({'male': 0, 'female': 1})


from sklearn.model_selection import train_test_split

# Define features and target variable
X = penguins_df.drop('species', axis=1).select_dtypes(include=['number'])
y = penguins_df['species']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)



from sklearn.ensemble import RandomForestClassifier

# Initialize the model
classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
classifier.fit(X_train, y_train)

import pickle
# Saving model to disk
pickle.dump(classifier, open('rf_model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('rf_model.pkl','rb'))
