FROM public.ecr.aws/docker/library/python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . ./
RUN pip install -r requirements.txt

RUN useradd appuser && chown -R appuser /app
USER appuser

EXPOSE 8000
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:8000", "portfolio.wsgi"]