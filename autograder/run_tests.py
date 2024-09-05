import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

if __name__ == '__main__':
    # Discover and run tests in the "tests" directory
    suite = unittest.defaultTestLoader.discover('tests')
    
    # Run the test suite and output results to a JSON file
    with open('/autograder/results/results.json', 'w') as f:
        JSONTestRunner(visibility='visible', stream=f).run(suite)
