"""A simple example with SimpleHTTPOperator

"""
from typing import Sequence

from airflow import DAG
from airflow.decorators import task
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import get_current_context
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.utils.dates import days_ago

_dag_doc_md = """
# A title for the DAG documentation

## A subtitle

This dag does that:

- get some data from disease.sh

"""


with DAG(
    "simplehttp01",
    schedule_interval="@once",
    start_date=days_ago(0),
    default_args={},
    tags=["http"],
    doc_md=_dag_doc_md,
) as dag:
    dum1 = DummyOperator(task_id="http1")

    rest_call_ex01 = SimpleHttpOperator(
        task_id="rest-call-ex01",
        http_conn_id="http-disease.sh",
        endpoint="/v3/covid-19/nyt/states",
        method="GET",
        log_response=True,
    )

    @task
    def transform(multiple_outputs=True) -> Sequence:
        """
        #### Transform task
        A simple Transform task which takes in the collection of order data and
        computes the total order value.
        """
        context = get_current_context()
        ti = context["ti"]
        data: Sequence = ti.xcom_pull(task_ids="rest-call-ex01", key="return_value")

        res = []

        for value in data:
            res.append(value)

        return data

    trans = transform()

    dum1 >> rest_call_ex01 >> trans
