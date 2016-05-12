# Flask-PiwikAPI

## Usage

```python
from flask import request, current_app as app

from piwikapi.tracking import PiwikTracker
from flask_piwikapi import FlaskRequest

piwik_tracker = PiwikTracker(app.config['PIWIK_SITE_ID'], FlaskRequest(request))
piwik_tracker.set_api_url(app.config['PIWIK_TRACKING_API_URL'])
piwik_tracker.set_token_auth(app.config['PIWIK_TOKEN_AUTH'])

piwik_tracker.do_track_page_view('Page Title')
```
