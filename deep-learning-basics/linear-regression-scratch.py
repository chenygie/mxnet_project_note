from IPython.display import set_matplotlib_formats
import matplot.pyplot as plt
from mxnet import autograd,nd
import random
num_inputs = 2
num_examples = 1000
true_w = [2,-3.4]
true_b = 4.2
features = nd.random.normal
