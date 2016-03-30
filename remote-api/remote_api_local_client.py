import os
import os.path as op
import sys
import json
appengine_path = op.expanduser('~/dev/google_appengine')
sys.path.append(appengine_path)

import dev_appserver
dev_appserver.fix_sys_path()    # otherwise fancy_urllib will not be found

service_account_key_path = op.join(op.abspath('.'), 'service_account_key.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_key_path

from google.appengine.ext.remote_api import remote_api_stub
from main import Log

project_id = project_id = json.load(open('../project_ids.json'))['remote-api']

remote_api_stub.ConfigureRemoteApiForOAuth(
    '%s.appspot.com' % project_id,
    '/_ah/remote_api')

from main import Log

print [l.text for l in Log.query().order(Log.date)]
