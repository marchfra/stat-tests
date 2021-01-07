from stat_tests import z_test
import uncertainties as u

def test_z_test():
	assert z_test.z_test(u.ufloat(0.01, 0.1)) == True
	assert z_test.z_test(u.ufloat(1, 0.1)) == False
	assert z_test.z_test(u.ufloat(0.01, 0.1), 10) == ValueError
	assert z_test.z_test('a', 0.05) == AssertionError