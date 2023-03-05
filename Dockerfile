## Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
#FROM python:3
## Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
#ENV PYTHONUNBUFFERED 1
## Устанавливает рабочий каталог контейнера — "app"
#WORKDIR /app
## Копирует все файлы из нашего локального проекта в контейнер
#ADD ./app .
## Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
#RUN pip install -r requirements.txt


#
#FROM python:3.9.12-slim
#WORKDIR /app/
#COPY . .
#RUN python3 -m pip install --no-cache-dir --no-warn-script-location --upgrade pip \
#    && python3 -m pip install --no-cache-dir --no-warn-script-location --user -r requirements.txt

#
FROM python:3.10.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /education
WORKDIR /education
COPY requirements.txt /education/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /education/


#FROM python:3
#ENV PYTHONUNBUFFERED 1
#ADD requirements.txt /education/
#WORKDIR /education/
#
#RUN pip install -r requirements.txt