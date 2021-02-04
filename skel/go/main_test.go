package main

import "testing"

// Test case structure
type testOne struct {
	result bool
}

func TestPlaceholder(t *testing.T) {
	// Test cases
	tests := []testOne{
		testOne{true},
	}

	// Tests execution
	for _, testCase := range tests {
		// Replace with the function to test, e.g.
		// if MyFunction() != testCase.result
		if !testCase.result {
			t.Errorf("Expected: %t\nGot: \n", testCase.result)
		}
	}

}
