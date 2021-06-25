FROM jenkins/jenkins:lts-jdk11
# if we want to install via apt
USER root
# RUN apt-get update \
#     && apt-get install -y software-properties-common \
#     && add-apt-repository -y --update ppa:ansible/ansible \
#     && apt-get install -y \
#         python3 \
#         python3-venv \
#         ansible
RUN apt-get update \
&& apt-get install -y \
    python3 \
    python3-venv \
    python3-pip
# drop back to the regular jenkins user - good practice
USER jenkins
RUN python3 -m pip install --user ansible
