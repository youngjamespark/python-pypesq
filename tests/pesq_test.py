import pypesq
import os

print("Current working directory = %s", os.getcwd())
pypesq.evaluate("dml\\1089-134686-0019_ori.pcm", "dml\\1089-134686-0019.pcm", 16000, "wb")
pypesq.evaluate("1089-134686-0000.wav", "1089-134686-0000.wav", 16000, "wb")
pypesq.evaluate("voice_8k_le.pcm", "voice_8k_le.pcm", 8000, "nb")
pypesq.evaluate("voice_8k_le.pcm", "voice_8k_le.711.pcm", 8000, "nb")
pypesq.evaluate("voice_8k_le.pcm", "voice_8k_le.729.pcm", 8000, "nb")
pypesq.evaluate("voice_8k_le.pcm", "voice_8k_le.723.pcm", 8000, "nb")