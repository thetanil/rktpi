broker_url = "pyamqp://"
result_backend = "rpc://"

task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
timezone = "Europe/Berlin"
enable_utc = True

task_annotations = {"tasks.add": {"rate_limit": "10/m"}}
