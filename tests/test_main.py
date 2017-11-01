import ci_dummy
import numpy


def test_arange_basic():
    n = 5
    assert ci_dummy.arange_basic(n).sum()==10
    assert ci_dummy.arange_basic(n).shape == (n,)


def test_double():
    assert ci_dummy.double(3)==6

def test_triple():
    assert ci_dummy.triple(3)==9