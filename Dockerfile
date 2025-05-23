FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

RUN chmod +x /app/deployment/*

ENTRYPOINT ["/app/deployment/entrypoint.sh"]
CMD ["/app/deployment/runserver.sh"]