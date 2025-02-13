FROM python:3.12

RUN pip3 install pytest==8.3.4

RUN pip3 install numpy

COPY primary.py /code/primary.py

COPY gcd_algorithm.py /code/gcd_algorithm.py

COPY test_primary.py /code/test_primary.py

COPY test_gcd.py /code/test_gcd.py

RUN chmod +rx /code/primary.py

ENV PATH="/code:$PATH"
