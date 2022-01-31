from pygcc.pygcc_utils import Henry_duan_sun, drummondgamma, Helgeson_activity, convert_temperature, calc_elem_count_molewt
import numpy as np
from collections import Counter

def test_Henry_duan_sun():
    """Test ln CO2 activity and molality at ionic strength of 0.5M with Duan_Sun."""
    expected = np.array([0.04888775, 1.17380618])
    actual = Henry_duan_sun(convert_temperature(150, Out_Unit = 'K'), 250, 0.5)
    actual = np.vstack(actual).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)

def test_water_activity():
    """Test Water activity, osmotic coefficient and NaCl mean activity coefficient at ionic strength of 0.5M with Drummond."""
    expected = np.array([0.98396138, 0.89749554, 0.60149936])
    actual = Helgeson_activity(150, 250, 0.5, Dielec_method = 'JN91')
    actual = np.vstack(actual).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)

def test_elemcounter():
    """Test the counting of the elemental composition of a substance"""
    expected = Counter({'O': 5.5, 'H': 2.0, 'S': 1, 'Cu': 1})
    actual = Counter(calc_elem_count_molewt("CuSO4.5H2O")[0])
    
    assert actual == expected, "Elements counted incorrectly!"
