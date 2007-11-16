from sympy import sympify, Symbol, exp, Integer, sin, cos, log
from sympy.abc import x, y
#from sympy.utilities.pytest import XFAIL


def test_439():
    v = sympify("exp(x)")
    x = Symbol("x")
    assert v == exp(x)
    assert type(v) == type(exp(x))
    assert str(type(v)) == str(type(exp(x)))

def test_sympify1():
    assert sympify("x") == Symbol("x")
    assert sympify("   x") == Symbol("x")
    assert sympify("   x   ") == Symbol("x")

def test_sympify2():
    class A:
        def _sympy_(self):
            return Symbol("x")**3

    a = A()

    assert sympify(a) == x**3
    assert a == x**3

def test_sympify3():
    assert sympify("x**3") == x**3
    assert sympify("1/2") == Integer(1)/2

def test_sage():
    # how to effectivelly test for the _sage_() method without having SAGE
    # installed?
    assert hasattr(x, "_sage_")
    assert hasattr(Integer(3), "_sage_")
    assert hasattr(sin(x), "_sage_")
    assert hasattr(cos(x), "_sage_")
    assert hasattr(x**2, "_sage_")
    assert hasattr(x+y, "_sage_")
    assert hasattr(exp(x), "_sage_")
    assert hasattr(log(x), "_sage_")