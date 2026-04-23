
from src.analysis.experiment_runner import Experiment

import pytest


def test_experiment_runner_valid_case():
    exp = Experiment(
        sorting_algorithm="insertion_sort",
        distribution="random",
        input_size=10,
        seed=42,
    )

    comparisons = exp.experiment_runner()

    assert isinstance(comparisons, int)
    assert comparisons >= 0


def test_experiment_runner_unknown_algorithm():
    exp = Experiment(
        sorting_algorithm="fake_sort",
        distribution="random",
        input_size=10,
        seed=42,
    )

    with pytest.raises(ValueError, match="Unknown algorithm"):
        exp.experiment_runner()


def test_experiment_runner_unknown_distribution():
    exp = Experiment(
        sorting_algorithm="insertion_sort",
        distribution="fake_distribution",
        input_size=10,
        seed=42,
    )

    with pytest.raises(ValueError, match="Unknown distribution"):
        exp.experiment_runner()


@pytest.mark.parametrize("sorting_algorithm", [
    "insertion_sort",
    "shell_sort1",
    "shell_sort2",
    "shell_sort3",
    "shell_sort4",
    "shell_sort5",
    "tim_sort",
])
@pytest.mark.parametrize("distribution", [
    "random",
    "almost_sorted",
    "two_alternating_runs",
])
def test_experiment_runner_all_combinations(sorting_algorithm, distribution):
    exp = Experiment(
        sorting_algorithm=sorting_algorithm,
        distribution=distribution,
        input_size=20,
        seed=42,
    )

    comparisons = exp.experiment_runner()

    assert isinstance(comparisons, int)
    assert comparisons >= 0