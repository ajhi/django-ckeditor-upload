import os
import urlparse

from django.http import HttpResponse
from django.template import RequestContext, Template
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.conf import settings
from django.core.files.storage import FileSystemStorage


SUCCESS_TEMPLATE = """
<html>
    <body>
        <script type="text/javascript">
            window.parent.CKEDITOR.tools.callFunction({{callback}}, "{{filename}}","");
        </script>
    </body>
</html>

"""



def test(request):
    return render_to_response('ckeditor_upload/test.html', {}, RequestContext(request))

@csrf_exempt
def upload(request):
    t = Template(SUCCESS_TEMPLATE)
    
    if hasattr(settings, 'CK_FILE_PATH'):
        ck_file_path = settings.CK_FILE_PATH
    else:
        ck_file_path = ''
    
    FILE_PATH = os.path.join(settings.MEDIA_ROOT, ck_file_path)
    FILE_URL = urlparse.urljoin(settings.MEDIA_URL, ck_file_path)
    
    if request.method == "POST":
        filesystem = FileSystemStorage(location=FILE_PATH, base_url=FILE_URL)
        try:
            uploaded_file = request.FILES['upload']
            filename = filesystem.save(uploaded_file.name, uploaded_file)
            ck_filename = filesystem.url(filename)
        except MultiValueDictKeyError:
            return HttpResponse(t.render())            
        try:
            callback = request.GET['CKEditorFuncNum']
        except:
            callback = ''
    else:
        return HttpResponse(t.render())
         
    rc = RequestContext(request, {
        'callback': callback,
        'filename': ck_filename,
    })
    

    return HttpResponse(t.render(rc))
        
