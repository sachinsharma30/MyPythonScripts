#This is the first part of the script. Installs docker

FROM  node:buster
RUN apt-get update 
RUN apt install docker.io -y
CMD nohup dockerd >/dev/null 2>&1 & sleep 10 && node /app/app.js

WORKDIR /usr/app/src

COPY fail_cf.tf ./
COPY WizCLIScriptnew.py ./

CMD ["python3", "./WizCLIScriptnew.py"]
