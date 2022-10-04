import pandas as pd
import numpy as np
import pickle
from sklearn import (
    model_selection,
    metrics
)
from sklearn.compose import make_column_selector as selector
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression


# params 
C = 1.0
n_splits = 5
output_file = f'model_C={C}.bin'

# Preparing Data
fp = ('https://raw.githubusercontent.com/alexeygrigorev/datasets'
      '/master/AER_credit_card_data.csv')

df = pd.read_csv(fp)
# print(df.sample(n=5))

# Mapping target variable
data, target = df.drop(columns=['card']), df['card'].map({'yes':1, 'no':0})

# Numerical and categorical features separation
numerical = selector(dtype_include=np.number)(data)
categorical = selector(dtype_include=object)(data)

# Split data set
df_full_train, df_test, y_full_train, y_test = model_selection.train_test_split(
    data,
    target,
    test_size=.2,
    random_state=1,
    # stratify=target
)
# training
# all_features 
all_features= numerical + categorical

def train(df_train, y_train, C=1.0, columns=all_features):
    dicts = df_train[all_features].to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    model = LogisticRegression(C=C, max_iter=1000, solver='liblinear')
    model.fit(X_train, y_train)
    
    return dv, model


def predict(df, dv, model, columns=all_features):
    dicts = df[columns].to_dict(orient='records')

    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred

# validation
print(f'doing validation with C={C}')
kfold = model_selection.KFold(
    n_splits=n_splits,
    shuffle=True,
    random_state=1
)

scores = []
fold = 0

for train_idx, dev_idx in kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_idx]
    df_dev = df_full_train.iloc[dev_idx]

    y_train = y_full_train.iloc[train_idx]
    y_dev = y_full_train.iloc[dev_idx]

    dv, model = train(df_train, y_train, C=C)
    y_pred = predict(df_dev, dv, model)

    auc = metrics.roc_auc_score(y_dev, y_pred)
    scores.append(auc)

    print(f'auc on fold {fold} is {auc}')
    fold += 1

print('validation results: ')
print(f"C={C} {np.mean(scores):.3f} +/- {np.std(scores):.3f}")

# training the final model

print('training the final model')
dv, model = train(
    df_full_train, 
    y_full_train,
    C=1.0,
    columns=all_features
)
y_pred = predict(df_test, dv, model)
auc = metrics.roc_auc_score(y_test, y_pred)

print(f'auc={auc}')

# Save the model
with open(output_file, 'wb') as f_out:
    pickle.dump((dv,model), f_out)


print(f'the model is saved to {output_file}')