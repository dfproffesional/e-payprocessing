FROM python:3.11.4-bullseye

# Update & Install dependences
RUN apt-get update && \
    apt-get install -y --no-install-recommends \ 
    sudo neovim curl wget sqlite3 &&\ 
    rm -rf /var/lib/apt/lists/*

ARG USERNAME=app
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME ;\
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME ;\
    echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

ADD requirements.txt /tmp
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

USER $USERNAME
RUN curl -s https://ohmyposh.dev/install.sh | sudo bash -s
RUN oh-my-posh font install FiraCode ;\
    sudo cp -r /root/themes ~/ ;\
    sudo chown $USERNAME:$USERNAME -R ~/themes ;\
    echo 'eval "$(oh-my-posh init bash --config ~/themes/clean-detailed.omp.json)"' >> ~/.bashrc