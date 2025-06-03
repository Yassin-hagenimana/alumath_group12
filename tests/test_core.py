from alumath_group12 import multiply_matrices

def test_multiply_matrices():
    # Test case 1: Basic multiplication
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    expected = [[19, 22], [43, 50]]
    assert multiply_matrices(a, b) == expected

    # Test case 2: Identity matrix
    a = [[1, 2], [3, 4]]
    b = [[1, 0], [0, 1]]
    expected = [[1, 2], [3, 4]]
    assert multiply_matrices(a, b) == expected

    # Test case 3: Zero matrix
    a = [[1, 2], [3, 4]]
    b = [[0, 0], [0, 0]]
    expected = [[0, 0], [0, 0]]
    assert multiply_matrices(a, b) == expected

    # Test case 4: Non-square matrices
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8], [9, 10], [11, 12]]
    expected = [[58, 64], [139, 154]]
    assert multiply_matrices(a, b) == expected

    # Test case 5: Empty matrix raises ValueError
    try:
        multiply_matrices([], [[1]])
        assert False, "Expected ValueError for empty first matrix"
    except ValueError:
        pass

    try:
        multiply_matrices([[1]], [])
        assert False, "Expected ValueError for empty second matrix"
    except ValueError:
        pass

    # Test case 6: Mismatched dimensions raises ValueError
    try:
        multiply_matrices([[1]], [[1], [2]])
        assert False, "Expected ValueError for mismatched dimensions"
    except ValueError:
        pass