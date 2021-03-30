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

when using it, please note that the sampling rate (frequency) should be 16000 or 8000. 

And using 8000 is supported for narrow band only.

>>> pesq_assess.evaluate("voice_8k_le.pcm", "voice_8k_le.pcm", 8000, "nb")

