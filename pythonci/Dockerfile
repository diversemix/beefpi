FROM sdhibit/rpi-raspbian 

RUN apt-get update
RUN apt-get install python python-webpy -y
RUN apt-get clean all

ADD example.py /example.py

CMD ["python", "/example.py", "4567"]
