import panda
import numpy

r = np.random.randn(100,3)
h, edges = np.histogramdd(r, bins = (5, 8, 4))
h.shape, edges[0].size, edges[1].size, edges[2].size