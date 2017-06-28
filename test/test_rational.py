from sklearn.linear_model import LinearRegression
import numpy as np

from sparsereg.rational import RationalFunctionWrapper


def test_rational_function_wrapper():

    def f(x):
        return 1/(1+x)
    
    x = np.linspace(2, 3, 10).reshape(-1, 1)
    y = f(x)

    model = RationalFunctionWrapper(LinearRegression())
    model.fit(x, y)
    np.testing.assert_almost_equal(model.intercept_, 1.0)
    np.testing.assert_allclose(model.coef_, np.array([0.0, -1]), atol=1e-10)

    np.testing.assert_almost_equal(model.predict(1), 0.5)