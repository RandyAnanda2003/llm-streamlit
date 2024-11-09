from dotenv import load_dotenv
import os


# api_key = ""
# watsonx_

load_dotenv()

# api_key = os.getenv("api_key")
# project_id = os.getenv ("watsonx_project_id")

globals()["api_key"] = os.getenv("api_key", None)
globals()["watsonx_project_id"] = os.getenv("project_id", None)


# print(api_key)
# print()
# print(project_id)