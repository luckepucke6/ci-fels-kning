import pytest

from miniforecast.features import min_max_scale, moving_average


def test_moving_average_window_two():
    assert moving_average([1, 2, 3, 4], 2) == [1.0, 1.6666666666666665, 2.333333333333333]


def test_moving_average_rejects_too_large_window():
    with pytest.raises(ValueError):
        moving_average([1, 2], 3)


def test_min_max_scale_range():
    assert min_max_scale([0, 5, 10]) == [0.0, 0.5, 1.0]


def test_min_max_scale_rejects_constant_input():
    with pytest.raises(ValueError):
        min_max_scale([4, 4, 4])
