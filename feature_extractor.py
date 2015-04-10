import numpy as np
from scipy.interpolate import UnivariateSpline

class FeatureExtractor(object):

    def __init__(self):
        pass

    def fit(self, X_dict, y):
        pass

    def transform(self, X_dict):

        return self.cleaner(np.array([self.transformer(x["light_points_r"]) for x in X_dict]))

    def transformer(self,y):
        x = np.linspace(0, 2 * np.pi, len(y))
        spl = UnivariateSpline(x,y)
        spl.set_smoothing_factor(.1)
        x = np.linspace(0, 2 * np.pi, 50)
        return spl(x)

    def cleaner(self,b):
        c=[]
        for x in b:
            if np.isnan(x[0]):
                c.append([0]*50)
            else:
                c.append(x)
        return c
