import tensorflow as tf
import pandas as pd

# read the data from the CSV file
data = pd.read_csv('it_issues.csv')

# define the feature and target variables
X = data.drop(['category'], axis=1)
y = data['category']

# one-hot encode the target variable
y = tf.keras.utils.to_categorical(y)

# create the model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(32, activation='relu', input_shape=(X.shape[1],)))
model.add(tf.keras.layers.Dense(32, activation='relu'))
model.add(tf.keras.layers.Dense(y.shape[1], activation='softmax'))

# compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# evaluate the model on the test set
test_loss, test_acc = model.evaluate(X_test, y_test)
print('Test accuracy:', test_acc)
