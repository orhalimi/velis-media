from sklearn import svm
from sklearn.model_selection import GridSearchCV
from parse_data import parse_data
from calc_error_pct import *
from gui_util import update_ui_message


class SVMHandler:
    """In this class you will implement the classifier and it's methods."""

    def __init__(self):
        """properties to save worker state during the run"""
        self.busy = 0
        self.has_trained = 0
        self.error_percentage = None
        self.svm = svm.SVC(C=1000)  # give better result then the default C
        update_ui_message("Ready")

    def train(self):
        update_ui_message("Start training...")

        self.busy = 1
        train_path = "./data/adult.data"
        x_metric, y_vectors = parse_data(train_path)
        self.svm.fit(x_metric, y_vectors)
        self.has_trained = 1
        self.busy = 0
        update_ui_message("Training done!")

    def predict(self):
        update_ui_message("Start testing...")

        self.busy = 1
        predict_path = "./data/adult.test"
        x_metric, y_vectors = parse_data(predict_path)
        y_predict = self.svm.predict(x_metric)
        self.error_percentage = calculate_error_percentage(y_vectors, y_predict)
        print(self.error_percentage)
        self.busy = 0
        update_ui_message("Testing done!")
