
def get_task_dict(json_string):
    try:
        task_dict = json.loads(json_string)
    except:
        return {}

    return task_dict