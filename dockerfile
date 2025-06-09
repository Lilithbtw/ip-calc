FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -ms /bin/sh www-user

COPY . .

RUN chown -R www-user:www-user /usr/src/app

USER www-user

EXPOSE 5000

CMD [ "python", "ipv4-check.py" ]