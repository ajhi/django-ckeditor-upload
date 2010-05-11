# Installation

* Put `ckeditor_upload` somewhere in your `PYTHON_PATH`
* Add `(r'^ckeditor_upload/$', include('ckeditor_upload.urls')),` in your urlpatterns
* Configure CKEditor with: `CKEDITOR.replace('textarea_name', { filebrowserUploadUrl: '/ckeditor_upload/upload/' });`