import matplotlib.pyplot as plt
import numpy as np
import os

from .experiment_runner import Experiment
from .registry import (ALGORITHMS, DISTRIBUTIONS)

INPUT_SIZES = [128, 256, 512, 1024, 2048, 4096, 8192, 16384]
SEEDS = [42, 43, 44, 45, 46]

def main():
    for distribution in DISTRIBUTIONS:
        plt.figure(figsize=(12, 7))

        for algorithm in ALGORITHMS:
            points = []

            for input_size in INPUT_SIZES:
                print(f"\n→ Running {algorithm} on {distribution}, n={input_size}")
                total = 0
                avg = 0

                for seed in SEEDS:
                    experiment = Experiment(algorithm, distribution, input_size, seed)
                    total += experiment.experiment_runner()
                
                avg = total / len(SEEDS)
                points.append((input_size, avg))
            
            x = [size for size, _ in points]
            y = [avg * 1e6 for _, avg in points]
            logx = np.log2(x)
            logy = np.log2(y)
            m, b = np.polyfit(logx, logy, 1)
            line = plt.loglog(x, y, 'o', markersize=8, label=f'{algorithm} ~ {m} log N + {b}')
            color = line[0].get_color()
            plt.loglog(x, 2 ** (m * logx + b), color=color, linewidth=2)
        
        plt.xscale("log", base=2)
        plt.yscale("log", base=2)
        plt.xlabel("log N")
        plt.ylabel("log T(N) (microseconds)")
        plt.title(f"Sorting {distribution} (Average of 10 samples per N)")
        plt.legend(fontsize=9, loc="upper left")

        os.makedirs("plots", exist_ok=True)
        filename = f"plots/{distribution}_loglog.png"
        plt.savefig(filename)

        plt.show()

if __name__ == "__main__":
    main()
