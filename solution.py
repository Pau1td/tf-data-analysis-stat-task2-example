import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 278913153 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    a = 0.026
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return 2*loc + 2*scale * norm.ppf(1 - alpha) + a, \
           2*loc + 2*scale * norm.ppf(p) + a
