FROM apache/spark:4.0.2-scala2.13-java17-python3-ubuntu

USER root

RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir \
        pyspark==4.0.2 \
        jupyterlab \
        notebook \
        ipykernel \
        pandas \
        matplotlib

ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3
ENV PATH=/usr/bin:$PATH

RUN mkdir -p /workspace/notebooks /workspace/src

EXPOSE 8888

CMD ["bash", "-c", "jupyter lab --ip=0.0.0.0 --no-browser --ServerApp.token='' --ServerApp.password='' --ServerApp.root_dir=/workspace --allow-root"]