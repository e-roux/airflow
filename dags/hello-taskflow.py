from airflow.decorators import dag, task
from airflow.operators.python import get_current_context
from airflow.utils.dates import days_ago


@dag(schedule_interval=None, start_date=days_ago(0))
def hello_taskflow_api(who: str = "world"):
    @task
    def whom() -> str:
        context = get_current_context()
        return context["params"]["who"].capitalize()

    @task
    def my_cust_print(value: str) -> str:
        return f"Hello {value}"

    whom_to_say_hello = whom()
    cust_print = my_cust_print(whom_to_say_hello)


hello = hello_taskflow_api()
