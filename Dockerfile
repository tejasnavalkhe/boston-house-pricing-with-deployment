# FROM ==> Select the base image
# COPY ==> Copy files from host to container
# WORKDIR ==> Set the working directory
# RUN ==> Execute commands
# EXPOSE ==> Expose ports
# CMD ==> Execute commands
# ENTRYPOINT ==> Execute commands
# ENV ==> Set environment variables
# VOLUME ==> Create mount points
# USER ==> Set the user
# LABEL ==> Set metadata
# ARG ==> Define build-time variables
# ONBUILD ==> Add a trigger instruction
# STOPSIGNAL ==> Set the stop signal
# SHELL ==> Set the default shell

FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app