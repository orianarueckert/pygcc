from pygcc import db_reader, solidsolution_thermo
import numpy as np

#%% specify the direct access thermodynamic database
ps = db_reader()

def test_calclogss():
    """Test All solid solutions."""
    expected = np.array([21.750590, 26.570902, 10.793372, 20.577152,  3.756792, 32.96363])
    actual = solidsolution_thermo(cpx_Ca = 0.5, X = 0.85, T = 30, P = 50, dbaccessdic = ps.dbaccessdic)
    actual = np.vstack((actual.AnAb_logK, actual.FoFa_logK, actual.EnFe_logK, actual.cpx_logK, 
    			actual.AlkFed_logK, actual.Biotite_logK)).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)



    
    