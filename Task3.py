"""Известно, что рост футболистов в сборной распределен нормально с дисперсией генеральной совокупности, 
равной 25 кв.см. Объем выборки равен 27, среднее выборочное составляет 174.2.
Найдите доверительный интервал для математического ожидания 
с надежностью 0.95."""

import math

# Известные значения
variance = 25
sample_mean = 174.2
sample_size = 27
confidence_level = 0.95

# Вычисление стандартного отклонения генеральной совокупности
population_std_dev = math.sqrt(variance)

# Вычисление значения Z для заданного уровня доверия
z_value = 1.96

# Вычисление доверительного интервала
margin_of_error = z_value * (population_std_dev / math.sqrt(sample_size))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

# Вывод результатов
print("Доверительный интервал (0.95):", round(confidence_interval[0], 2), round(confidence_interval[1], 2) )


"""вывод
Доверительный интервал (0.95): 172.31 176.09"""