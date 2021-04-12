from airflow import DAG

dag_1 = DAG("02_1_DAG_scope")


def my_function():
    dag_2 = DAG("02_2_DAG_scope")


# dag2 in a local scope and not in the DAG list
my_function()
