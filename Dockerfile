FROM okdocker/pynode:latest

RUN pip install pytest requests bs4

WORKDIR /app
COPY . .

RUN yarn install

EXPOSE 3030
CMD ["bash", "test.sh"]
