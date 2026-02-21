import scipy;
import pandas as pd;
from sklearn.datasets import load_iris;

d = pd.DataFrame(load_iris().data, columns=load_iris().feature_names);
print("DataFrame:", d);
print("Mean:", d.mean());
print("Median:", d.median());
print("Mode:", d.mode());
m