from datetime import datetime

from airflow.decorators import dag
from airflow.operators.dummy import DummyOperator


@dag(start_date=datetime(2021, 1, 1))
def my_dag_2():

    task_1 = DummyOperator(task_id="task_1")
    task_2 = DummyOperator(task_id="task_2")
    task_1 >> task_2


bla = my_dag_2()
