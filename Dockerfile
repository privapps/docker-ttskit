FROM ubuntu:20.04

ENV WORKDIR /workspace
ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:$WORKDIR:${PATH}

RUN apt-get update -y --fix-missing && apt-get install -y libsndfile1 python3 pip portaudio19-dev ffmpeg

RUN pip install --no-cache-dir -U pyaudio pyworld numba==0.51.2 ttskit

RUN cd /usr/bin ; ln -s python3 python

RUN while [ `python -c 'import ttskit;ttskit.tts("1")' ; echo $?` -ne 0 ]; do sleep 1 ; done

ENTRYPOINT ["bash"]

