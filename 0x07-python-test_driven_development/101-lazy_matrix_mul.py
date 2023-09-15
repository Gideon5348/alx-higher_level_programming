#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b using NumPy.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        np.ndarray: The resulting matrix of the multiplication.
    """
    # Convert input lists to NumPy arrays
    np_a = np.array(m_a)
    np_b = np.array(m_b)

    # Check if the matrices can be multiplied
    if np_a.shape[1] != np_b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication using NumPy
    result = np.dot(np_a, np_b)

    return result
