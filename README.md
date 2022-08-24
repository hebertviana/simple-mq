# Simple project to write and get message in IBM MQ using python

Download cliente for python

https://developer.ibm.com/articles/mq-downloads/#python

Direct link

[Redist (grab & go) MQ Downloads](https://ibm.biz/IBM-MQC-Redist-LinuxX64targz)


Unzip the file and add the path to the LD_LIBRARY_PATH variable.

```sh
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./9.3.0.0-IBM-MQC-Redist-LinuxX64/lib64
```

# setting up the environment

Download IBM MQ Dev version

[mqadv_dev930_linux_x86-64](https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/messaging/mqadv/mqadv_dev930_linux_x86-64.tar.gz)

Installing IBM MQ Client

```sh
sudo ./mqadv_dev930_linux_x86-64/MQServer/mqlicense.sh
sudo rpm -ivh ./mqadv_dev930_linux_x86-64/MQServer/MQSeriesRuntime-9.3.0-0.x86_64.rpm
sudo rpm -ivh ./mqadv_dev930_linux_x86-64/MQServer/MQSeriesGSKit-9.3.0-0.x86_64.rpm
sudo rpm -ivh ./mqadv_dev930_linux_x86-64/MQServer/MQSeriesClient-9.3.0-0.x86_64.rpm
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

# Credits

[PyMQI](https://zato.io/pymqi/)

[IBM](https://www.ibm.com/docs/en/ibm-mq/9.3)
