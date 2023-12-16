from roboflow import Roboflow
import os
import json

api_key = os.getenv("zgUkZWodt1Ed3DMrHUS4")

if api_key is not None:
    rf = Roboflow(api_key=api_key)
    workspace = rf.workspace(os.environ["machinelearningusdbryan"])
else:
    print("Roboflow API key not found.")

# rf = Roboflow(api_key=os.environ["zgUkZWodt1Ed3DMrHUS4"])

projects = ["mug-detector-eocwp", "mug-detector-0akq7"]

def generate_and_train(project: str, configuration: dict) -> None:
    """
    Generate a version of a model and commence training for the new version.
    """
    rf_project = workspace.project(project)

    version_number = rf_project.generate_version(configuration)

    project_item = workspace.project(project).version(version_number)

    project_item.train()

with open("configuration/starter.json", "r") as f:
    configuration = json.load(f)


generate_and_train(projects[0], configuration)

# def apply_multiple_experiments(project: str) -> None:
#     """
#     For each configuration in the "configurations" folder,
#     generate and train a modelfor the specified project.
#     """
#     for configuration in os.listdir("configurations"):
#         with open(f"configurations/{configuration}") as f:
#             configuration = json.load(f)

#         generate_and_train(project, configuration)

# for project in projects:
#     apply_multiple_experiments(project)