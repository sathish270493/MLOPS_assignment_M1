import unittest
from sklearn.linear_model import LinearRegression


class TestModel(unittest.TestCase):
    def test_model_instance(self):
        model = LinearRegression()
        self.assertIsInstance(model, LinearRegression)

    def test_training(self):
        from sklearn.datasets import make_regression
        X, y = make_regression(n_samples=100, n_features=1, noise=0.1, random_state=42)
        model = LinearRegression()
        model.fit(X, y)
        self.assertGreater(len(model.coef_), 0)


if __name__ == "_main_":
    unittest.main()
