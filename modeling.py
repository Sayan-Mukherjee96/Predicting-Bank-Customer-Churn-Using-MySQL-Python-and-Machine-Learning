from sklearn.preprocessing import LabelEncoder
df = df.copy()
categorical_input_cols = ['Gender']
label_encoders = {}
for column in categorical_input_cols:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column])

from sklearn.model_selection import train_test_split
x = df.drop(['Exited'], axis=1)
Y = df['Exited']

x_train, x_test, Y_train, Y_test = train_test_split(x,Y, test_size =0.3, random_state=42)

from sklearn.preprocessing import MinMaxScaler, StandardScaler
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(random_state=42)
logreg.fit(x_train_scaled, Y_train)

result = logreg.predict(x_test_scaled)

from sklearn import tree
clf = tree.DecisionTreeClassifier(max_depth=3,criterion='gini')

DTree=clf.fit(x_train_scaled,Y_train)
result2=DTree.predict(x_test_scaled)
result2

from sklearn.ensemble import RandomForestClassifier
result3 = RandomForestClassifier(random_state = 42)
result3.fit(x_train_scaled, Y_train)

from sklearn.metrics import classification_report
print(classification_report(Y_test, result)) # Logistic Regression
print(classification_report(Y_test, result2))  # Decision Tree Classifier
rf_pred = result3.predict(x_test_scaled)
print(classification_report(Y_test, rf_pred)) #RandomForestClassifier

Y_lable = logreg.predict_proba(x_test_scaled)[:,1]
Y_lable

from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(Y_test, Y_lable)
thresholds

def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], "k--")
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Logistic Regression ROC Curve')

fpr, tpr, thresholds = roc_curve(Y_test, logreg.predict_proba(x_test_scaled)[:,1])
plt.figure(figsize=(7,7)); 
plot_roc_curve(fpr, tpr)
plt.show()

def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], "k--")
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Decision Tree ROC Curve')

fpr, tpr, thresholds = roc_curve(Y_test, DTree.predict_proba(x_test_scaled)[:,1])
plt.figure(figsize=(7,7)); 
plot_roc_curve(fpr, tpr)
plt.show()

def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], "k--")
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Random Forest ROC Curve')

fpr, tpr, thresholds = roc_curve(Y_test, result3.predict_proba(x_test_scaled)[:,1])
plt.figure(figsize=(7,7)); 
plot_roc_curve(fpr, tpr)
plt.show()

optimal_idx = np.argmax(tpr - fpr)
optimal_threshold = thresholds[optimal_idx]
print("Optimal threshold is:",optimal_threshold)

from sklearn.metrics import confusion_matrix
cnf_matrix = confusion_matrix(Y_test, result)


plt.figure(figsize=(7,7))
ax = sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'viridis_r', fmt = 'd')
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)
plt.xlabel('Prediction')
plt.ylabel('Actual')
plt.show()

cnf_matrix = confusion_matrix(Y_test, result2)


plt.figure(figsize=(7,7))
ax = sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, cmap = 'viridis_r', fmt = 'd')
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)
plt.xlabel('Prediction')
plt.ylabel('Actual')
plt.show()

cnf_matrix = confusion_matrix(Y_test, rf_pred)

plt.figure(figsize=(7,7))
sns.heatmap(
    pd.DataFrame(cnf_matrix),
    annot=True,
    cmap='viridis_r',
    fmt='d'
)

plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()
