import unittest
import numpy as np
from spectralcluster import refinement


class TestCropDiagonal(unittest.TestCase):
  """Tests for the CropDiagonal class."""

  def test_3by3_matrix(self):
    matrix = np.array([[1, 2, 3], [3, 4, 5], [4, 2, 1]])
    adjusted_matrix = refinement.CropDiagonal().refine(matrix)
    expected = np.array([[3, 2, 3], [3, 5, 5], [4, 2, 4]])
    self.assertTrue(np.array_equal(expected, adjusted_matrix))


class TestGaussianBlur(unittest.TestCase):
  """Tests for the GaussianBlur class."""

  def test_3by3_matrix(self):
    matrix = np.array([[1.0, 2.0, 3.0], [3.0, 4.0, 5.0], [4.0, 2.0, 1.0]])
    adjusted_matrix = refinement.GaussianBlur(sigma=1).refine(matrix)
    expected = np.array([[2.12, 2.61, 3.10], [2.76, 2.90, 3.06],
                         [3.16, 2.78, 2.46]])
    self.assertTrue(np.allclose(expected, adjusted_matrix, atol=0.01))


class TestRowWiseThreshold(unittest.TestCase):
  """Tests for the RowWiseThreshold class."""

  def test_3by3_matrix_percentile(self):
    matrix = np.array([[0.5, 2.0, 3.0], [3.0, 4.0, 5.0], [4.0, 2.0, 1.0]])
    adjusted_matrix = refinement.RowWiseThreshold(
        p_percentile=0.5,
        thresholding_soft_multiplier=0.01,
        thresholding_with_row_max=False).refine(matrix)
    expected = np.array([[0.005, 2.0, 3.0], [0.03, 4.0, 5.0], [4.0, 2.0, 0.01]])
    self.assertTrue(np.allclose(expected, adjusted_matrix, atol=0.001))

  def test_3by3_matrix_row_max(self):
    matrix = np.array([[0.5, 2.0, 3.0], [3.0, 4.0, 5.0], [4.0, 2.0, 1.0]])
    adjusted_matrix = refinement.RowWiseThreshold(
        p_percentile=0.5,
        thresholding_soft_multiplier=0.01,
        thresholding_with_row_max=True).refine(matrix)
    expected = np.array([[0.005, 2.0, 3.0], [3.0, 4.0, 5.0], [4.0, 2.0, 0.01]])
    self.assertTrue(np.allclose(expected, adjusted_matrix, atol=0.001))


class TestSymmetrize(unittest.TestCase):
  """Tests for the Symmetrize class."""

  def test_3by3_matrix(self):
    matrix = np.array([[1, 2, 3], [3, 4, 5], [4, 2, 1]])
    adjusted_matrix = refinement.Symmetrize().refine(matrix)
    expected = np.array([[1, 3, 4], [3, 4, 5], [4, 5, 1]])
    self.assertTrue(np.array_equal(expected, adjusted_matrix))


class TestDiffuse(unittest.TestCase):
  """Tests for the Diffuse class."""

  def test_2by2_matrix(self):
    matrix = np.array([[1, 2], [3, 4]])
    adjusted_matrix = refinement.Diffuse().refine(matrix)
    expected = np.array([[5, 11], [11, 25]])
    self.assertTrue(np.array_equal(expected, adjusted_matrix))


class TestRowWiseNormalize(unittest.TestCase):
  """Tests for the RowWiseNormalize class."""

  def test_3by3_matrix(self):
    matrix = np.array([[0.5, 2.0, 3.0], [3.0, 4.0, 5.0], [4.0, 2.0, 1.0]])
    adjusted_matrix = refinement.RowWiseNormalize().refine(matrix)
    expected = np.array([[0.167, 0.667, 1.0], [0.6, 0.8, 1.0], [1.0, 0.5,
                                                                0.25]])
    self.assertTrue(np.allclose(expected, adjusted_matrix, atol=0.001))


if __name__ == "__main__":
  unittest.main()
