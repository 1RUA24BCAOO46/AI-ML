 
from sklearn.neighbors import KNeighborsClassifier 
# Create k-NN model with k=3 (look at 3 nearest neighbours) 
knn = KNeighborsClassifier(n_neighbors=3) 
# Train the model 
knn.fit(X_train, y_train) 
# Predict on test set 
y_pred = knn.predict(X_test) 
# Check accuracy 
accuracy = knn.score(X_test, y_test) 
print(f"Test accuracy: {accuracy * 100:.2f}%")
