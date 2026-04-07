import os
import sys
import pickle

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(models, X_train, y_train, X_test, y_test, params=None):
    try:
        report = {}

        for model_name, model in models.items():
            model_params = params.get(model_name, {}) if params else {}
            if model_params:
                grid_search = GridSearchCV(
                    estimator=model,
                    param_grid=model_params,
                    cv=3,
                    n_jobs=-1,
                    verbose=0,
                )
                grid_search.fit(X_train, y_train)
                best_model = grid_search.best_estimator_
                models[model_name] = best_model
                model = best_model
            else:
                model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)