from pygcc import iapws95, ZhangDuan, water_dielec
import numpy as np

print('Testing water equation of state and dielectric properties')
def test_iapws95():
    """Test TP for iapws95."""
    expected = np.array([867.2595, -60368.41787, -65091.03895,  
    			 25.14869,  4.96478e-03,  50.00000,  200.000])
    actual = iapws95(T = 200., P = 50)
    actual = np.vstack((actual.rho, actual.G, actual.H, actual.S, actual.V, actual.P, actual.TC)).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)


def test_iapws95_Sat():
    """Test Sat for iapws95."""

    expected = np.array([584.147147, 688.423692,  55.463085])
    actual = iapws95(P = 100)
    actual = np.vstack((actual.TK, actual.rhosl, actual.rhosv)).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)
    
    
def test_ZhangDuan_Trho():
    """Test Trho for deep earth conditions."""
    expected = np.array([2.87150846e+03, -5.90809497e+04,  2.32829711e-05, -6.75206166e-04])
    actual = ZhangDuan(T = 200, rho = 995)
    actual = np.vstack((actual.P, actual.G, actual.drhodP_T, actual.drhodT_P)).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)



def test_ZhangDuan_TP():
    """Test TP for deep earth conditions."""

    expected = np.array([1145.3075, -54631.5351, 2.328297e-05, -0.0004889424])
    actual = ZhangDuan(T = 25, P = 5000)
    actual = np.vstack((actual.rho, actual.G, actual.drhodP_T, actual.drhodT_P)).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)
 

def test_FGL97():
    """Test FGL97 formulation."""

    expected = np.array([6.99159964e+01,  9.88035048e-01,  5.34108322e-01,  
    			3.32567100e-01, 4.08852828e-02,  6.87578006e-01,  
    			2.37680041e+00,  1.65567606e+01, -1.34077776e+01,  
    			3.54401490e-02, -3.21210312e-01])
    actual = water_dielec(T = 50, P = 'T', Dielec_method = 'FGL97')
    actual = np.vstack((actual.E, actual.rhohat, actual.Ah, actual.Bh, actual.bdot, actual.Adhh, 
    			actual.Adhv, actual.Bdhh, actual.Bdhv, actual.dEdP_T, actual.dEdT_P)).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)


def test_JN91():
    """Test JN91 formulation."""

    expected = np.array([6.98067350e+01,  9.88035048e-01,  5.35372646e-01,  3.32836364e-01,
			4.08852828e-02,  6.83521450e-01,  2.53510753e+00,  1.63934761e+01,
		       -1.81646484e+01,  3.69937281e-02, -3.19932779e-01])
    actual = water_dielec(T = 50, P = 'T', Dielec_method = 'JN91')
    actual = np.vstack((actual.E, actual.rhohat, actual.Ah, actual.Bh, actual.bdot, actual.Adhh, 
    			actual.Adhv, actual.Bdhh, actual.Bdhv, actual.dEdP_T, actual.dEdT_P)).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)

def test_DEW():
    """Test DEW formulation."""

    expected = np.array([3.83200994e+01,  9.21831483e-01,  7.17645213e-01,  3.58598417e-01,
			4.45257922e-02,  1.15231321e+00,  7.02321141e+00,  5.22936799e+01,
		       -6.60804366e+01,  2.71527951e-02, -9.87632403e-02])
    actual = water_dielec(T = 200, P = 1000, Dielec_method = 'DEW')
    actual = np.vstack((actual.E, actual.rhohat, actual.Ah, actual.Bh, actual.bdot, actual.Adhh, 
    			actual.Adhv, actual.Bdhh, actual.Bdhv, actual.dEdP_T, actual.dEdT_P)).ravel()
    
    np.testing.assert_allclose(expected, actual, rtol=1e-6, atol=0)
