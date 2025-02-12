FROM python:3.12.8-slim

WORKDIR /llm-summarizer

COPY requirements.txt setup.py README.md ./
COPY summarizer ./summarizer

RUN pip install -e . --use-pep517

CMD ["tail", "-f", "/dev/null"]