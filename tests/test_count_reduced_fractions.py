# %%
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1].resolve()))
from utils import count_reduced_fractions


def main():
    test_data = [
        [(0, 1, 2), 1],
        [(0, 1, 3), 2],
        [(0, 1, 4), 2],
        [(0, 1, 5), 4],
        [(1, 2, 2), 1],
        [(1, 2, 3), 2],
        [(1, 2, 4), 2],
        [(1, 2, 5), 4],
    ]
    for (m, n, frac), res in test_data:
        calc_res = count_reduced_fractions(m, n, frac)
        print(f"# frac {frac} in [{m},{n}]: {calc_res} ({calc_res==res})")


if __name__ == "__main__":
    main()
