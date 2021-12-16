broker_url = "pyamqp://"
result_backend = "rpc://"
# result_backend = "db+sqlite:///results.sqlite"
result_persistent = False


task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
timezone = "Europe/Berlin"
enable_utc = True

# For Flower
# address = "192.168.0.37"

# task_annotations = {"tasks.add": {"rate_limit": "10/m"}}
# task_annotations = {"tasks.add": {"rate_limit": "10/m"}}
