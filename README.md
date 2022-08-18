# Simple project to write and get message in IBM MQ using python

Download cliente for python

https://developer.ibm.com/articles/mq-downloads/#python

Direct link

[Redist (grab & go) MQ Downloads](https://ibm.biz/IBM-MQC-Redist-LinuxX64targz)


# setting up the environment

Unzip the file and add the path to the LD_LIBRARY_PATH variable.

```sh
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/${USER}/simple-mq/ibm-mq/lib64
```

Install dependencies

```sh
poetry install
```

# Usage simple-mq

```sh
poetry shell 

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/${USER}/simple-mq/ibm-mq/lib64

python -i main.py

# Writing 1000 messages
put_mensagem(1000)
```

Open new terminal

```sh
poetry shell 

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/${USER}/simple-mq/ibm-mq/lib64

python -i main.py

# Get message with wait
get_mensagem_wait()
```

# add-on running IBM MQ

The official IBM project can be used

[mq-container](https://github.com/ibm-messaging/mq-container)
