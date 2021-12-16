import os
import pytest


def test_template_folders():
    assert os.path.exists("data")
    assert os.path.exists("saved_models")
    assert os.path.exists("src/model")
    assert os.path.exists("src/tests")
    assert os.path.exists("src/tests/test_files")
    assert os.path.exists("src/tests/test_results")
    assert os.path.exists("src/train")
    assert os.path.exists("src/utils")