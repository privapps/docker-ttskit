FROM privapps/ttskit:0.1.6_base

COPY run.sh /
COPY run.py /
RUN mkdir -p $WORKDIR ; chmod a+rwx $WORKDIR run.sh

ENTRYPOINT ["/run.sh"]