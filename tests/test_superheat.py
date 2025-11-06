# tests/test_superheat.py
import pytest
from src.superheat import superheat_temp, celsius_to_fahrenheit

# مقادیر مرجع از جدول بخار (ASME / IAPWS): 
# در p = 100 bar, h = 3300 kJ/kg → T ≈ 485.4 °C (دقیق: 485.42 با PYXSteam)
TEST_CASES = [
    (100, 3300, 485.42),   # بویلر فشار بالا
    (10,  2800, 190.00),   # فشار پایین‌تر
    (200, 3500, 620.37),   # شرایط سخت‌تر
]

def test_superheat_temp_accuracy():
    """Test against known steam table values (tolerance: ±0.1°C)"""
    for p, h, expected_c in TEST_CASES:
        actual_c = superheat_temp(p, h, "C")
        assert abs(actual_c - expected_c) < 0.1, f"p={p}, h={h}: expected {expected_c}, got {actual_c}"

def test_celsius_to_fahrenheit():
    """Basic unit conversion sanity check"""
    assert abs(celsius_to_fahrenheit(0) - 32.0) < 1e-6
    assert abs(celsius_to_fahrenheit(100) - 212.0) < 1e-6
    assert abs(celsius_to_fahrenheit(485.42) - 905.756) < 0.01

def test_unit_parameter():
    """Ensure backward compatibility and case insensitivity"""
    t1 = superheat_temp(100, 3300, "C")
    t2 = superheat_temp(100, 3300, "c")
    t3 = superheat_temp(100, 3300)  # default
    assert t1 == t2 == t3

    t_f = superheat_temp(100, 3300, "F")
    assert abs(t_f - 905.756) < 0.01
