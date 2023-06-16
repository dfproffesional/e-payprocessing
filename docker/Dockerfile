FROM python:3.11.4-bullseye

ARG USERNAME=app
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    echo export PATH=$PATH:/home/$USERNAME/.local/bin >> /home/$USERNAME/.bashrc && \
    echo export PATH=$PATH:/home/$USERNAME/.local/bin >> /home/$USERNAME/.profile

ADD . /app
RUN chown -R app:app /app

WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt
