import pandas as pd
from scipy.stats import norm


chat_id = 1253313260

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
    # Рассчитаем доли успеха для контрольной и тестовой групп
    p_x = x_success / x_cnt
    p_y = y_success / y_cnt

    # Рассчитаем разность долей
    diff = p_y - p_x

    # Рассчитаем стандартную ошибку
    se = np.sqrt((p_x * (1 - p_x) / x_cnt) + (p_y * (1 - p_y) / y_cnt))

    # Рассчитаем значение z-статистики
    z_stat = diff / se

    # Рассчитаем p-значение для z-статистики
    p_value = 1 - norm.cdf(z_stat)

    # Сравним p-значение с уровнем значимости
    return p_value < 0.1
