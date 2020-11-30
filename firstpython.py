# This is my new Python file I guess

import numpy as np
import matplotlib.pyplot as plt

def Yahtzee():
  roll = np.random.randint(1,7,(1,5))
  return roll
  plt.plot(roll, range(1,6))
