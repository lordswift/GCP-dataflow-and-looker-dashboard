from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "project001-440621"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bqloadandtest-sk",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://bk-df-md-sk/udf.js",
        "JSONPath": "gs://bk-df-md-sk/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "project001-440621:basketball_dataset_sk.ranking",
        "inputFilePattern": "gs://bkt-ranking-data-sk/rankings.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://bk-df-md-sk",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)

