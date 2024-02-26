FROM docker.io/library/python:3.11-bullseye AS base

CMD /bin/bash
COPY ./cert.conf /jupyter_server.conf 
RUN apt-get update
RUN apt-get install -y unixodbc-dev
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -config /jupyter_server.conf -keyout /etc/ssl/jupyter_server.key -out /etc/ssl/certs/jupyter_server.pem
RUN useradd --create-home --shell /bin/bash jupyter
USER jupyter
WORKDIR /home/jupyter
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install psycopg2
RUN export PATH="/home/jupyter/.local/bin:$PATH"
#RUN mkdir -p persistent/notebooks persistent/data persistent/helpers
RUN mkdir -p non_persistent/notebooks non_persistent/data non_persistent/helpers

USER root
RUN chown -R jupyter /home/jupyter
RUN chown jupyter /etc/ssl/jupyter_server.key
RUN chown jupyter /etc/ssl/certs/jupyter_server.pem

FROM base
LABEL org.opencontainers.image.source https://github.com/jeremiah-carlson/dev-tools
USER jupyter
RUN cd ~
CMD [ ".local/bin/jupyter", "notebook", "--no-browser", "--port", "8080", "--ip", "0.0.0.0", "--certfile", "/etc/ssl/certs/jupyter_server.pem", "--keyfile", "/etc/ssl/jupyter_server.key", "--NotebookApp.token=''", "--NotebookApp.password='sha256:627caf014a1c:ecc3da90960e8ae18e2e7d9bd55a3788e59cfb49d328e33d8e1f153cd88071f5'"]
#ENTRYPOINT [ "/bin/bash", "-c", "sleep infinity" ]

EXPOSE 443
EXPOSE 8080