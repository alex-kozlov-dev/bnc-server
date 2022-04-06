import os
from dotenv import load_dotenv

load_dotenv()


def settings_processor(request):
    if request.user.is_authenticated:
        preview_url = os.getenv('PREVIEW_URL', '/')
        deploy_hook = os.getenv('DEPLOY_HOOK', '/')
    else:
        preview_url = '/'
        deploy_hook = '/'

    return {'preview_url': preview_url, 'deploy_hook': deploy_hook}
