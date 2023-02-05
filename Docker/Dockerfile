FROM ubuntu:latest 			// better write version, example: ubuntu:22.04 it's more stable

WORKDIR /app

COPY . /app

RUN apt get update && \		// better write commands in this style, because it's use less layers
	apt get upgrade && \
	apt get install apache2 -y && \
	echo "ServerName 127.0.0.1" >> /etc/apache2/apache2.conf

EXPOSE 80

CMD ["apache2ctl", "-D", "FOREGROUND"]