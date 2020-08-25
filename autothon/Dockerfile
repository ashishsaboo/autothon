FROM ubuntu:19.10
FROM python:3.6

RUN apt update
RUN apt-get -y install allure
RUN apt-get -f install
RUN apt-get install -f -y fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libatk1.0-0 libdrm2 libgbm1 libnspr4 libnss3 libx11-xcb1 libxcb-dri3-0 xdg-utils
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN apt-get install -f

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

ADD start.sh ./

RUN chmod 777 ./start.sh

CMD ["sh","start.sh"]

#CMD ["behave", "-f allure_behave.formatter:AllureFormatter"," -o ./output/allure-reports"," ./features"," --tags=@example"]

#CMD ["allure", "serve ./output/allure-reports"]

