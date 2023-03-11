FROM python:3
MAINTAINER Nghi Nguyen <nnguyen@oberlin.edu>
# Environment variables
ENV OBIESOURCETOKEN=<TOKEN GOES HERE>
# Create directory
RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot

# Finish creating environment
COPY . /usr/src/bot
RUN pip3 install -r requirements.txt

# Entry Point
CMD ["python3", "./obiesourcebot.py"]