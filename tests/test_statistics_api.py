from pywmapi.statistics.api import *
import pytest


@pytest.mark.skip("Statistics seem to have been removed from v2 API")
def test_get_statistic():
    get_statistic("mirage_prime_systems")
    get_statistic("heavy_trauma")
