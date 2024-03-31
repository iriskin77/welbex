FROM python:3.10-slim

RUN mkdir /welbex

WORKDIR /welbex

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod a+x /welbex/start.sh

ENTRYPOINT ["./start.sh"]
