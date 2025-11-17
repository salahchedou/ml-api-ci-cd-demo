from typing import List
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


class IrisModel:
    def __init__(self):
        self._model = RandomForestClassifier(random_state=42)
        self._train()

    def _train(self):
        data = load_iris()
        X, y = data.data, data.target
        self.target_names = data.target_names
        self._model.fit(X, y)

    def predict_class(self, features: List[float]) -> str:
        pred = self._model.predict([features])[0]
        return self.target_names[pred]


iris_model = IrisModel()
