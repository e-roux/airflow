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

- https://jvns.ca/blog/2016/10/10/what-even-is-a-container/
- https://docs.metaflow.org/introduction/why-metaflow
- https://en.wikipedia.org/wiki/Linux_namespaces
