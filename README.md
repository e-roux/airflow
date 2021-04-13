# Airflow tutorial

This tutorial is based on the [Apache Airflow
documentation](https://airflow.apache.org/docs).


## Quickstart

Repository must be cloned with [submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

```bash
git clone --recurse-submodules <REPO_URL>
```

Once cloned, everything should be triggered with

```terminal
make up
```

Manual start-up can be alternatively done:

```terminal
# User set-up:
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

# DB initilization:
docker-compose up airflow-init

# Start-up
docker-compose up
```

## Source:

- [Data’s Inferno: 7 Circles of Data Testing Hell with Airflow](https://medium.com/wbaa/datas-inferno-7-circles-of-data-testing-hell-with-airflow-cef4adff58d8)
- [Airflow summit 2020: Testing Airflow workflows](https://www.youtube.com/watch?v=ANJnYbLwLjE)
- https://livebook.manning.com/book/data-pipelines-with-apache-airflow
- https://docs.metaflow.org/introduction/why-metaflow
- https://en.wikipedia.org/wiki/Linux_namespaces
- https://github.com/microservices-demo/microservices-demo
- https://jvns.ca/blog/2016/10/10/what-even-is-a-container/
- https://www.ibm.com/cloud/learn/containerization
- https://www.ibm.com/cloud/learn/docker
- https://www.pluralsight.com/blog/it-ops/docker-containers-take-over-world
- https://semaphoreci.com/blog/kubernetes-vs-docker

## Div

Colors are from
[Solarized](https://en.wikipedia.org/wiki/Solarized_(color_scheme))
