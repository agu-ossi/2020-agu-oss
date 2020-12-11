import pytest

# Module to be tested
import agu_oss


def test_division():
    assert agu_oss.divide(6, 2) == 3

    with pytest.raises(TypeError):
        agu_oss.divide(6, '2')
