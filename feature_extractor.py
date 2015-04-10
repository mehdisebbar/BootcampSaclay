from scipy.interpolate import UnivariateSpline
import numpy as np

class FeatureExtractor(object):

    def __init__(self):
        pass

    def fit(self, X_dict, y):
        pass

    def transform(self, X_dict):

        return np.array([self.transformer(x["light_points_r"]) for x in X_dict])

    def transformer(self,y):
        x = np.linspace(0, 2 * np.pi, len(y))
        spl = UnivariateSpline(x,y)
        spl.set_smoothing_factor(.1)
        x = np.linspace(0, 2 * np.pi, 50)
        return spl(x)
