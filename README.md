# Divy_Trips_tripdata 

Divy Trips is a fictitious cab hailing company in New York City. Divy has been collecting individual trip data from 2009 to 2016. The data is large and is stored in a clickhouse database (https://github.demo,trial.altinity.cloud:8443/play). The business seeks to generate monthly aggregated data and load in a DWH to
facilitate business analytics and informed decision-making.

## Project
 You have been hired as a data engineer, and your first task is to orchestrate a pipeline to achieve this objective. You are to use modular coding and appropriate version control for the solution you develop, to facilitate code maintenance, and collaboration with your future team members.

## Tasks
• ﻿﻿Explore the trip data on Clickhouse
• ﻿﻿Extract the trip data and load to a staging area on an on-prem database.
• ﻿﻿Create a production environment and develop procedures to load aggregate tables to show the following monthly metrics (average trip count, average trip duration, average trip fare)
• ﻿﻿Push your code to a new Github repository,
• ﻿﻿Pull the codebase from the github repository.
• ﻿﻿Create a branch and refactor the code to load data incrementally and implement an orchestration to load the data daily.
• ﻿﻿Commit your changes to your branch and create a pull request to merge your changes to the main branch (codebase).
• ﻿﻿Orchestrate the incremental load pipeline using Windows task Scheduler.

## Solution Architecture
[Apache_airflow_Clickhouse_Diagram drawio](https://github.com/user-attachments/assets/bc7f0cf4-2079-44ca-829d-e1d3a7cadf8e)


## Part 2
## Introduction to Apache Flow

## Introduction
In the previous part, we successfully built an ETL data pipeline. However, running & managing this pipeline will pose some challenges:
• ﻿﻿We will have to manually run this pipeline or depend on inefficientCRON jobs.
• ﻿﻿We can't monitor our pipeline so we're unable to detect where and when there is a failure in the execution of tasks.
• ﻿﻿We will be unable to manage complex task dependencies.
• ﻿﻿We will be unable to backfill/re-run historical data.

## Apache Airflow
Airflow is an open-source orchestration framework used to programmatically author, schedule and monitor data pipelines or workflows.
• ﻿﻿Airflow was created & open-sourced by Airbb in 2015 as an orchestrator for Dag-based, schedulable data pipelines.
• ﻿﻿Airflow is built & runs in Python.
• ﻿﻿Airflow is used by more than 200 companies including: Google, Stripe, Paypal.


## Why Airflow?
• ﻿﻿Automate the execution of series of tasks in a data pipeline.
• ﻿﻿With Airflow we can schedule when tasks should be executed.
• ﻿﻿With Airflow we can monitor execution of tasks in a pipeline. This helps us identify an error or a breakdown in task execution so this can be fixed.
• Airflow provides a web Ul for visualizing the execution of tasks/processes in a pipeline.
• We can setup a notification system to receive notification of successful or failed jobs in Airflow.
• ﻿﻿With Airflow, we can backfill or process historical jobs.


## Directed Acyclic Graphs (DAGs)
Graphs: Describe entities & the relationships between them. They are powerful concepts in modeling complex systems.
E.g. Social Network graphs, A graph of Airline routes.
[View](https://github.com/user-attachments/assets/c4672a09-199a-4465-ab0e-1b92c20b1d3e)


## Directed Acyclic Graphs (DAGs)
DAGs are a special subset of graphs in which the edges between nodes have a specific direction, and no cycles exist. When we say "no cycles exist" what we mean is the nodes can't create a path back to themselves.


## Airflow DAGs
Airflow uses the concept of a Directed Acyclic Graphs (Dags) to define a workflow or pipeline.


## DAGS
A Dag is a collection of all the tasks you want to run, organized in a way that reflects their relationships & dependencies.
Graph of a DAG:
DAG definition in Airflow:


## Operators & Tasks
Operators determine what actually gets done in a dag. It describes a single task in a workflow.
Tasks: once an operator is instantiated, it is referred to as a task.


## Operator Categories
Operators are classified into 3 categories:
• ﻿﻿Sensors: A type of operator that keeps running until a certain criteria is met. E.g. waiting for an external file. Examples includes: HDFS Sensor,
  Check operator.
• ﻿﻿Operators: This type of operator triggers certain action(execute python function, run bash command). Example includes: BashOperator, Python Operator, BigQueryOperator.
• ﻿﻿Transfers: This type of operator moves data from one location to another. Example includes: MySqlToHiveTransfer, S3ToRedshift Transfer.


## Task Dependencies
Task dependencies is simply defining the order in which the tasks in a DAG should be executed in.
Task dependencies are set using:
1. ﻿﻿﻿The set _upstream & set_downstream operators like this: tl.set_downstream(t2). This means task t2 depends on task +1.
2. ﻿﻿﻿The bit shift operator (<< & >>) tl >> 12.
This means task t2 depends on task +1


## Dag Runs
Every Dag in Airflow is scheduled to run at certain interval of time. This is known as the execution time. A Dag run is created for every execution time.


## Task Instances
Task instances are the tasks that belongs to each Dag run.
The status of a Dag run or task instances can either "queued", "running",
"failed", "skipped" or "up for retry". These information is logged in Airflow's metadata database.

## Airflow UI DAG Graph view



## Steps to Structuring Airflow DAG file
To build your data pipeline in Airflow, you define a DAG file in a python script. Below are the 5 steps involved in structuring an Airflow DAG file:
• ﻿﻿Step 1: Import modules
• ﻿﻿Step 2: Specify default arguments
• ﻿﻿Step 3: Instantiate a DAG
• ﻿﻿Step 4: Define tasks using operators
• ﻿﻿Step 5: Setup dependencies between tasks.


 ## ﻿﻿Step 1: Import modules
Import the Python modules & Airflow dependencies needed for the workflow:


## Step 2: Specify default arguments


 ## ﻿﻿Step 3: Instantiate a DAG

 ## Step 4: Define tasks using operators

## Operators & Tasks
• Operators determine what actually gets done in a dag. It describes a single task in a workflow.
• Tasks: once an operator is instantiated, it is referred to as a task.

## Step 5: Setup dependencies
Finally, we setup the dependency between each tasks of the DAG:


