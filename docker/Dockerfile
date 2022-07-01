FROM python:3.8.0

WORKDIR /app

# install poetry
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
RUN pip install poetry
COPY ./pyproject.toml .
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY localminima localminima 
COPY docker/entrypoint.sh entrypoint.sh
COPY examples .
RUN mkdir artifacts

ENTRYPOINT ["./entrypoint.sh"]
