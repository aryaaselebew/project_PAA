import random
import time
import matplotlib.pyplot as plt
import numpy as np

n_values = [100, 150, 200, 250, 300, 350, 400, 500]
stambuk_last_3 = 87 
max_value = 250 - stambuk_last_3
seed = 42

def generate_array(n, max_value):
    random.seed(seed)
    return [random.randint(0, max_value) for _ in range(n)]

def is_unique(arr):
    return len(arr) == len(set(arr))

def measure_time(n, max_value):
    random.seed(seed)
    arr = generate_array(n, max_value)

    start_time = time.time()
    is_unique(arr)
    worst_case_time = time.time() - start_time

    avg_times = []
    for _ in range(10):
        start_time = time.time()
        is_unique(arr)
        avg_times.append(time.time() - start_time)

    average_case_time = sum(avg_times) / len(avg_times)

    return worst_case_time, average_case_time

results = []
for n in n_values:
    worst_time, avg_time = measure_time(n, max_value)
    results.append((n, worst_time, avg_time))

with open("worst_avg.txt", "w") as f:
    f.write("n\tworst_case\taverage_case\n")
    for n, worst, avg in results:
        f.write(f"{n}\t{worst:.6f}\t{avg:.6f}\n")

n_vals, worst_cases, avg_cases = zip(*results)
plt.figure(figsize=(10, 6))
plt.plot(n_vals, worst_cases, label="Worst Case", marker="o")
plt.plot(n_vals, avg_cases, label="Average Case", marker="o")
plt.xlabel("n (Number of Elements)")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time for Worst and Average Cases")
plt.legend()
plt.grid()
plt.savefig("execution_time_plot.jpg")
plt.show()

print("All files generated successfully.")
