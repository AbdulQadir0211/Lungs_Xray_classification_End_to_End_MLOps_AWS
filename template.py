import os
from pathlib import Path

project_name = "Xray"


list_of_files = [
    
    f"{project_name}/__init__.py",
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/s3_operation.py",

    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_training.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",

    #f"{project_name}/configuration/__init__.py",
    #f"{project_name}/constants/__init__.py",

    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact.py",

    #f"{project_name}/exception/__init__.py",
    #f"{project_name}/logger/__init__.py",

    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    #f"{project_name}/pipeline/prediction_pipeline.py",
    
    #f"{project_name}/utils/__init__.py",
    #f"{project_name}/utils/main_utils.py",
    
    "app.py",
    "requirements.txt",
    ".github/workflow/ci.yaml",
    ".github/workflow/main.yaml",
    "Dockerfile",
    ".dockerignore",
    ".gitignore",
    "demo.py",
    "setup.py",
    #"config/model.yaml",
    #"config/schema.yaml",
    "test/__init__.py",
    "test/unittest/__init__.py",
    "test/integrationtest/__init__.py",
    "bentofile.yaml",

]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
    else:
        print(f"file is already present at : {filepath}")