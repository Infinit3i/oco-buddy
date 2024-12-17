import unittest

def run_all_tests():
    # Discover and load tests from the 'Testing' directory
    loader = unittest.TestLoader()
    suite = loader.discover('Testing')

    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == "__main__":
    run_all_tests()
