from pygcc import db_reader, supcrtaq, heatcap
import numpy as np

#%% specify the direct access thermodynamic database
ps = db_reader()

def test_mineralheatcap_SUPCRT():
    """Test solid mineral and gases heat capacity equation."""
    expected = np.array([-11782.47165818, 8.58416135])
    actual = heatcap( T = 100, P = 50, Species = 'H2S(g)', Species_ppt = ps.dbaccessdic['H2S(g)'], method = 'supcrt')
    actual = np.vstack((actual.dG, actual.dCp)).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)

    expected = np.array([-205292.75498942, 12.34074489])
    actual = heatcap( T = 100, P = 50, Species_ppt = ps.dbaccessdic['Quartz'], Species = 'Quartz', method = 'supcrt')
    actual = np.vstack((actual.dG, actual.dCp)).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)


def test_mineralheatcap_HF():
    """Test solid mineral Haas and Fisher heat capacity equation."""
    expected = np.array([-960440.79915641, 57.46776903])
    actual = heatcap( T = 100, P = 50, Species_ppt = ps.dbaccessdic['ss_Anorthite'], Species = 'ss_Anorthite', method = 'HF76')
    actual = np.vstack((actual.dG, actual.dCp)).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)



def test_supcrtaq():
    """Test HKF equation."""
    expected = np.array([-9221.81721068])
    actual = supcrtaq( 100, 50, ps.dbaccessdic['H2S(aq)'], Dielec_method = 'JN91')
    actual = np.vstack(actual).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)


    
    