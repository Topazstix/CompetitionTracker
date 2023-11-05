FROM continuumio/miniconda3:latest

## Switch shell
SHELL ["/bin/bash", "-c"]

## Update and upgrade base sys
RUN apt update && \
    apt upgrade -y 

## Unsure if this is necessary but adding for now
RUN useradd -m managerApp && \
    apt install -y sudo && \
    usermod -aG sudo managerApp
RUN echo 'managerApp ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

