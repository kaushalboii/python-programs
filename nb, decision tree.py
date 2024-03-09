import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load the SMS spam dataset
df = pd.read_csv('path/to/your/dataset.csv')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Vectorize the SMS text using CountVectorizer
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Naïve Bayes Classifier
naive_bayes_model = MultinomialNB()
naive_bayes_model.fit(X_train_vectorized, y_train)
nb_predictions = naive_bayes_model.predict(X_test_vectorized)

# Decision Tree Classifier
decision_tree_model = DecisionTreeClassifier()
decision_tree_model.fit(X_train_vectorized, y_train)
dt_predictions = decision_tree_model.predict(X_test_vectorized)

# Support Vector Machine Classifier
svm_model = SVC()
svm_model.fit(X_train_vectorized, y_train)
svm_predictions = svm_model.predict(X_test_vectorized)

# Rule-Based Filtering
def rule_based_filter(text):
    # Implement your rule-based filtering logic here
    # Return 'spam' or 'ham' based on the rules
    pass

# Apply rule-based filtering to the test set
rule_based_predictions = X_test.apply(rule_based_filter)

# Gaussian Naïve Bayes Classifier
gaussian_naive_bayes_model = GaussianNB()
gaussian_naive_bayes_model.fit(X_train_vectorized.toarray(), y_train)
gnb_predictions = gaussian_naive_bayes_model.predict(X_test_vectorized.toarray())

# Evaluate models
print("Naïve Bayes Accuracy:", accuracy_score(y_test, nb_predictions))
print("Decision Tree Accuracy:", accuracy_score(y_test, dt_predictions))
print("SVM Accuracy:", accuracy_score(y_test, svm_predictions))
print("Rule-Based Filtering Accuracy:", accuracy_score(y_test, rule_based_predictions))
print("Gaussian Naïve Bayes Accuracy:", accuracy_score(y_test, gnb_predictions))

# You can also print additional evaluation metrics
print("\nNaïve Bayes Classification Report:\n", classification_report(y_test, nb_predictions))
print("\nDecision Tree Classification Report:\n", classification_report(y_test, dt_predictions))
print("\nSVM Classification Report:\n", classification_report(y_test, svm_predictions))
print("\nRule-Based Filtering Classification Report:\n", classification_report(y_test, rule_based_predictions))
print("\nGaussian Naïve Bayes Classification Report:\n", classification_report(y_test, gnb_predictions))
