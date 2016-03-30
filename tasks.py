import json
from invoke import task, run


@task
def deploy(project):
    project_id = json.load(open('project_ids.json'))[project]
    run('appcfg.py -A %s update %s/' % (project_id, project))

    print 'http://%s.appspot.com/' % project_id
