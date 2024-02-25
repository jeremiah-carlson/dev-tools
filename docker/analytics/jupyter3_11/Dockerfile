FROM docker.io/library/python:3.11-bullseye AS base

CMD /bin/bash
RUN useradd --create-home --shell /bin/bash jupyter
USER jupyter
WORKDIR /home/jupyter
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
RUN export PATH="/home/jupyter/.local/bin:$PATH"
RUN mkdir notebooks data helpers

USER root
RUN chown -R jupyter /home/jupyter

FROM base
LABEL org.opencontainers.image.source https://github.com/jeremiah-carlson/dev-tools
USER jupyter
RUN cd ~
CMD [ ".local/bin/jupyter", "notebook", "--no-browser", "--port", "8080", "--ip", "0.0.0.0", "--NotebookApp.token=''", "--NotebookApp.password=''"]
#ENTRYPOINT [ "/bin/bash", "-c", "sleep infinity" ]

EXPOSE 8080