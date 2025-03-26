# Orpheus CPP

[![PyPI - Version](https://img.shields.io/pypi/v/orpheus-cpp.svg)](https://pypi.org/project/orpheus-cpp)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/orpheus-cpp.svg)](https://pypi.org/project/orpheus-cpp)

-----

## Installation

```console
pip install orpheus-cpp
```

You also need to install the `llama-cpp-python` package separately. This is because llama-cpp-python does not ship pre-built wheels on PyPi.

Don't worry, you can just run one of the following commands:

### Linux/Windpes
```console
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
```

### MacOS with Apple Silicon
```console
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/metal
```

## Usage

```python
from orpheus_cpp import OrpheusCpp
from scipy.io.wavfile import write


orpheus = OrpheusCpp()

text = "I really hope the project deadline doesn't get moved up again."

# output is a tuple of (sample_rate (24_000), samples (numpy int16 array))
sample_rate, samples = orpheus.tts(text, options={"voice_id": "tara"})
write("output.wav", sample_rate, samples.squeeze())
```

## Streaming Sync

```python
for sample_rate, samples in orpheus.stream_tts_sync(text, options={"voice_id": "tara"}):
    write("output.wav", sample_rate, samples.squeeze())
``` 

## Streaming Async

```python
async for sample_rate, samples in orpheus.stream_tts(text, options={"voice_id": "tara"}):
    write("output.wav", sample_rate, samples.squeeze())
``` 

## Async FastRTC Demo

After installing `orpheus-cpp`, install `fastrtc` and run the following command:

```console
python -m orpheus_cpp
```

Then go to `http://localhost:7860` and you should see the demo.

## License

`orpheus-cpp` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
