from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime,timedelta

default_args={
    'owner':'airflow',
    'depends_on_past':False,
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':1,
    'retry_delay': timedelta(minutes=1),}
dag=DAG('aniplaylist',
default_args=default_args,
description='Aniruth top 10 playlist',
start_date=datetime(2024,12,10),
schedule_interval=timedelta(minutes=5),
catchup=False,)
run_process=BashOperator(task_id='run_process',bash_command="bash /home/skullcrusher/wrapper_script.sh ",
                         dag=dag)