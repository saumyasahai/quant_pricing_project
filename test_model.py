
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pricing.black_scholes import black_scholes_price


def test_call_price():
    price = black_scholes_price(100, 100,1,0.05,0.2, option_type = 'call')
    assert abs(price-10.45)<0.1
def test_put_price():
    price =black_scholes_price(100, 100,1,0.05,0.2, option_type = 'put')
    assert abs(price -5.57)<0.1
