from celeryapp import celeryInstance

@celeryInstance.task()
def make_file(fname, content):
    with open(fname, "w") as f:
        f.write(content)
