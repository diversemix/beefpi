FROM sdhibit/rpi-raspbian 

RUN apt-get update && apt-get install wget unzip -y

RUN wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip && \
	unzip ngrok-stable-linux-arm.zip && \
	mv ngrok /usr/local/sbin

RUN apt-get clean all 
ADD config.yml /config.yml

CMD ["/usr/local/sbin/ngrok", "start", "githook", "-log=stdout", "--config=/config.yml"]
