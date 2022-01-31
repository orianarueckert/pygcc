from pygcc import db_reader, supcrtaq, heatcap, heatcapusgscal
import numpy as np

#%% specify the direct access thermodynamic database
ps = db_reader()

def test_mineralheatcap():
    """Test solid mineral and gases heat capacity equation."""
    expected = np.array([-11782.47165818, 8.58416135])
    actual = heatcap( 100, 50, ps.dbaccessdic['H2S(g)'])
    actual = np.vstack(actual).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)

    expected = np.array([-205292.75498942, 12.34074489])
    actual = heatcap( 100, 50, ps.dbaccessdic['Quartz'], spec_name = 'Quartz')
    actual = np.vstack(actual).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)


def test_mineralheatcapusgscal():
    """Test solid mineral Haas and Fisher heat capacity equation."""
    expected = np.array([-960440.79915641, 57.46776903])
    actual = heatcapusgscal( 100, 50, ps.dbaccessdic['ss_Anorthite'])
    actual = np.vstack(actual).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)



def test_supcrtaq():
    """Test HKF equation."""
    expected = np.array([-9221.81721068])
    actual = supcrtaq( 100, 50, ps.dbaccessdic['H2S(aq)'], Dielec_method = 'JN91')
    actual = np.vstack(actual).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)


    
    