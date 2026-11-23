"""Public tests for Lab 11. Hidden tests are harder!"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
import lab11 as lab  # noqa: E402

import numpy as np

def test_perceptron_and():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    w = lab.train_perceptron(X, [0, 0, 0, 1])
    assert list(lab.perceptron_predict(w, X)) == [0, 0, 0, 1]
