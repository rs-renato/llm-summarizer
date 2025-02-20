FROM python:3.12.8-slim

WORKDIR /llm-summarizer

COPY requirements.txt setup.py README.md ./

RUN pip install --no-cache-dir -r requirements.txt

COPY summarizer ./summarizer
RUN pip install --no-cache-dir -e . --use-pep517

EXPOSE 3007

CMD ["tail", "-f", "/dev/null"]