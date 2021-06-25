FROM jenkins/jenkins:lts-jdk11
# if we want to install via apt
USER root
RUN echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
RUN apt-get update \
    && apt-get install -y \
        python3 \
        python3-venv \
        ansible
RUN apt-get update \
&& apt-get install -y \
    python3 \
    python3-venv \
    python3-pip
# drop back to the regular jenkins user - good practice
USER jenkins
RUN python3 -m pip install --user ansible
