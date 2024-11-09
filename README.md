# MiniRAG

This is a minimal implementation of the RAG moddel for question answering.


## Requirments

- Python 3.8 or later

### Install python using MiniConda 

1) Download and install MiniConda from [here](https://docs.anaconda.com/miniconda/#quick-command-line-install)

2) create environment using the following command: 
``` bash
    conda create -n mini-rag1 python=3.8
```
3) Activate the environment:
``` bash
    conda activate mini-rag1
```
### (Optional)Setup your commandline for better readability:
``` bash
    export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```
## Installation

### Install required packages:
``` bash
    pip install -r requirements.txt 
```
### Setup the environment varibles
``` bash
    cp .env.example .env
```
Set your evnironment varibles in the `.env` file. 

### Run Docker Compose Service

``` bash
    cd docker
    cp .env.example .env
``` 
-update `.env` with your credentials

``` bash
    cd docker
    sudo docker compose up -d
```


## Run FastAPI server:
``` bash
    uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
