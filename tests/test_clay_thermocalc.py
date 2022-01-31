from pygcc import db_reader, calclogKclays
import numpy as np

#%% specify the direct access thermodynamic database
ps = db_reader()

def test_claylogK():
    """Testing log K clay."""
    expected = np.array([57.56820225])
    actual = calclogKclays(50, 'T', *['Clinochlore', '3', '2', '0', '0', '5', '0', '0', '0', '0'], group = '14A', dbaccessdic = ps.dbaccessdic)[0]
    actual = np.vstack(actual).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)



    
    