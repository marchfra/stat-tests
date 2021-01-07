from stat_tests import z_test
import uncertainties as u

def test_z_test():
	assert z_test.z_test(u.ufloat(0.1, 0.1)) == f'The input value 0.10+/-0.10 is compatible with 0 with a significance of 5.0%'
	assert z_test.z_test(u.ufloat(1, 0.1)) == f'The input value 1.00+/-0.10 is not compatible with 0 with a significance of 5.0%'
	assert z_test.z_test('a', 0.05) == AssertionError