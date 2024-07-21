# Lung X-ray Classification End to End (MLops) Deep Learning Project.

## Tools used
1. AWS S3
2. BentoMl



## Workflows

- constants
- config_enity
- artifact_enity
- components
- pipeline
- main

# How to setup:

```bash
conda create -n lungs python=3.8 -y
```

```bash
conda activate lungs
```

```bash
pip install -r requirements.txt
```


```bash
setup AWS CLI
link: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

```

```bash
aws configure
```

```bash
AWS_ACCESS_KEY_ID=***

AWS_SECRET_ACCESS_KEY= ***

AWS_REGION = us-east-1
```

# Data Ingestion Workflow
![Data Ingestion Diagram](/home/abdul-qadir/dlproject/workflow_diagram/01_Data_Ingestion_flowchart.png)


# Data Transformation Workflow

![Data Transformation Diagram](/home/abdul-qadir/dlproject/workflow_diagram/02_Data_transformation_flowchart.png)


# Model Training Pipeline

![Model Training Pipeline](/home/abdul-qadir/dlproject/workflow_diagram/03_model_training_flowchart.png)


