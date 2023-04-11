import pandas as pd
import numpy as np
from scipy import stats


chat_id = 317456038 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t_stat, p_value = stats.ttest_1samp(x, 300)
    return (t_stat < 0) and (p_value / 2 < 0.08)
