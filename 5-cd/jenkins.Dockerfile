FROM jenkins/jenkins:lts-jdk11
# if we want to install via apt
USER root
RUN apt-get update \
    && apt-get install software-properties-common \
    && add-apt-repository --yes --update ppa:ansible/ansible \
    && apt-get install -y \
        python3 \
        python3-venv \
        ansible
# drop back to the regular jenkins user - good practice
USER jenkins
