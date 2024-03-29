#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Example DAG demonstrating the usage of the TaskGroup."""

import random

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
from airflow.utils.helpers import chain
from airflow.utils.task_group import TaskGroup

NOPS = random.choice((5, 6, 7, 8))

with DAG(dag_id="example_task_group", start_date=days_ago(2), tags=["example"]) as dag:
    start = DummyOperator(task_id="start")

    with TaskGroup("section_0", tooltip="Tasks for section_01") as section_0:

        chain([DummyOperator(task_id=f"task_{i}") for i in range(NOPS)])

    with TaskGroup("section_1", tooltip="Tasks for section_1") as section_1:
        task_1 = DummyOperator(task_id="task_1")
        task_2 = BashOperator(task_id="task_2", bash_command="echo 1")
        task_3 = DummyOperator(task_id="task_3")

        task_1 >> [task_2, task_3]

    with TaskGroup("section_2", tooltip="Tasks for section_2") as section_2:
        task_1 = DummyOperator(task_id="task_1")

        with TaskGroup(
            "inner_section_2", tooltip="Tasks for inner_section2"
        ) as inner_section_2:
            task_2 = BashOperator(task_id="task_2", bash_command="echo 1")
            task_3 = DummyOperator(task_id="task_3")
            task_4 = DummyOperator(task_id="task_4")

            [task_2, task_3] >> task_4

    end = DummyOperator(task_id="end")

    start >> section_0 >> section_1 >> section_2 >> end
