# python-pesq

PESQ (Perceptual Evaluation of Speech Quality) Wrapper for Python Users

This code is designed for numpy array specially.

# Requirements

    C compiler
    numpy
    SWIG

# Build and Install
$ python setup.py install

# Example for narrow band and wide band
The extension ".wav" and ".pcm" are suported. The reference and degraded files don't have the same extensions.
In case of ".wav", header and tail data are excluded from evaluation.
In case of ".pcm", the information except data should not be included in the file.

when using it, please note that the sampling rate (frequency) should be 16000 or 8000. 
And using 8000 is supported for narrow band only.

>>> pypesq.evaluate("voice_8k_le.pcm", "voice_8k_le.pcm", 8000, "nb")

