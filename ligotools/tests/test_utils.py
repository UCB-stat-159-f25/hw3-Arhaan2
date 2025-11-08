import numpy as np
import pytest
from pathlib import Path
from scipy.io import wavfile as _wavfile

from ligotools.utils import whiten, write_wavfile, reqshift


def test_whiten_with_flat_psd_scales_signal():
    """
    If PSD(f) == 1 for all f, whiten() should just scale the signal by sqrt(2*dt),
    because irfft(rfft(x)) == x and our implementation multiplies by that norm.
    """
    fs = 4096.0
    dt = 1.0 / fs
    x = np.random.RandomState(0).randn(4096)

    # Flat PSD interpolator: returns ones for any frequency array
    interp_psd = lambda f: np.ones_like(f)

    y = whiten(x, interp_psd, dt)
    expected = x * np.sqrt(2.0 * dt)

    assert y.shape == x.shape
    # Tight tolerance because it’s pure FFT/invFFT arithmetic
    np.testing.assert_allclose(y, expected, rtol=1e-12, atol=1e-12)


def test_reqshift_moves_sinusoid_peak_frequency():
    """
    Shift a cosine from f0 to f0+fshift and check the FFT peak lands near the new frequency.
    """
    fs = 4096
    N = 4096
    t = np.arange(N) / fs
    f0 = 50.0
    fshift = 100.0

    x = np.cos(2.0 * np.pi * f0 * t)
    y = reqshift(x, fshift=fshift, sample_rate=fs)

    Y = np.fft.rfft(y)
    freqs = np.fft.rfftfreq(N, 1.0 / fs)

    # ignore DC when searching for the peak
    peak_idx = np.argmax(np.abs(Y[1:])) + 1
    peak_freq = freqs[peak_idx]

    assert abs(peak_freq - (f0 + fshift)) <= (fs / N) + 1e-6  # within one FFT bin


def test_write_wavfile_roundtrip(tmp_path: Path):
    """
    Write a short waveform to WAV and read it back: dtype, length and peak should be sensible.
    """
    fs = 4096
    t = np.arange(4096) / fs
    x = 0.5 * np.sin(2 * np.pi * 220 * t)  # any valid audio-like signal

    out = tmp_path / "test.wav"
    p = write_wavfile(out, fs, x, normalize=True, dtype="int16")

    assert p.exists() and p.is_file()

    sr, data = _wavfile.read(p)
    assert sr == fs
    assert data.dtype == np.int16
    assert data.ndim == 1
    assert data.size == x.size

    # Because we normalized, the peak should be around 0.9 * 32767 (allow off-by-1 quantization)
    peak = int(0.9 * 32767)
    assert abs(int(np.max(np.abs(data))) - peak) <= 2
