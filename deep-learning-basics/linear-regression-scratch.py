from IPython.display import set_matplotlib_formats
import matplot.pyplot as plt
from mxnet import autograd,nd
import random
num_inputs = 2
num_examples = 1000
true_w = [2,-3.4]
true_b = 4.2
features = nd.random.normal(scale = 1,shape=(num_examples,num_inputs))
labels = true_w[0] * features[i][0] + true_w * features[i][1] + true_b
labels += nd.random.normal(scale=0.1,shape=(labels.shape))

def set_figsize(figsize=(5,4)):
    set_matplotlib_formats('retina')
    plt.rcParams['figure.figsize'] = figsize
def features_show():
    set_figsize(figsize=(6,5))
    plt.scatter()
