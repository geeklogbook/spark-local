FROM bitnami/spark:3.3.2-debian-11-r10

USER root

RUN /opt/bitnami/python/bin/pip install --upgrade pip && \
    /opt/bitnami/python/bin/pip install pyspark==3.3.2 notebook ipykernel pandas matplotlib

ENV PYSPARK_PYTHON=/opt/bitnami/python/bin/python3
ENV PYSPARK_DRIVER_PYTHON=/opt/bitnami/python/bin/python3
ENV PYTHONPATH=/opt/bitnami/spark/python:/opt/bitnami/spark/python/lib/py4j-0.10.9.5-src.zip:$PYTHONPATH
ENV PATH=/opt/bitnami/python/bin:$PATH

USER 1000

WORKDIR /opt/bitnami/spark