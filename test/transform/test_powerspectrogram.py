import numpy as np
import pytest

from praudio.transform.powerspectrogram import PowerSpectrogram
from utils import sample_signal


@pytest.fixture
def power_spectrogram():
    return PowerSpectrogram(100, 50, 75, "hann", 2)


def test_loader_instance_is_instantiated_correctly(power_spectrogram):
    assert isinstance(power_spectrogram, PowerSpectrogram)
    assert power_spectrogram.frame_length == 100
    assert power_spectrogram.hop_length == 50
    assert power_spectrogram.win_length == 75
    assert  power_spectrogram.power == 2
    assert power_spectrogram.window == "hann"
    assert power_spectrogram.name == "power_spectrogram"


def test_power_spectrogram_is_extracted(power_spectrogram, sample_signal):
    """
    GIVEN a Signal object
    AND an power spectrogram object
    WHEN the signal is passed to process
    THEN the power spectrogram is extracted
    AND the modified Signal object with the new power spectrogram is returned
    """
    signal = power_spectrogram.process(sample_signal)
    assert signal.name == "power_spectrogram"
    assert type(signal.data) == np.ndarray
    assert len(signal.data.shape) == 2
    assert type(signal.data[0][0]) == np.float_


def test_array_is_raised_to_power(power_spectrogram):
    array = np.array([1, 2, 4])
    array = power_spectrogram._raise_to_power(array)
    assert np.array_equal(array, np.array([1, 4, 16]))