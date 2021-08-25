import os
import shutil
from pathlib import Path

import pytest

from praudio.preprocessors.batchfilepreprocessor import BatchFilePreprocessor
from utils_preprocess import file_preprocessor


DUMMY_DATASET_DIR = Path(Path(__file__).parent.parent, "dummydataset")


@pytest.fixture
def batch_file_preprocessor(file_preprocessor):
    return BatchFilePreprocessor(file_preprocessor, "savedummy")


def test_batch_file_preprocessor_instantiated(batch_file_preprocessor):
    assert isinstance(batch_file_preprocessor, BatchFilePreprocessor)
    assert batch_file_preprocessor.save_dir == "savedummy"


def test_audio_dataset_is_batch_preprocessed(batch_file_preprocessor):
    """
    GIVEN a batch file processor
    AND a dir with audio data
    WHEN preprocess is called
    THEN all the audio files are processed recursively
    AND they are stored recursively on disk
    """
    batch_file_preprocessor.preprocess(DUMMY_DATASET_DIR)
    assert os.path.isfile(os.path.join("savedummy", "dummy.npy"))
    assert os.path.isfile(os.path.join("savedummy", "dir1", "dir2",
                                       "dummy.npy"))
    shutil.rmtree("savedummy")

def test_save_path_is_inferred_correctly(batch_file_preprocessor):
    save_path = batch_file_preprocessor._infer_save_path(
                        "dummydir1/dummydir2/dummydir3/file.wav",
                        "dummydir1/dummydir2")
    assert save_path == "savedummy/dummydir3/file"