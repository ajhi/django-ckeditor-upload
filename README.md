# Installation

* Put `ckeditor_upload` somewhere in your `PYTHON_PATH`
* Add `(r'^ckeditor_upload/$', include('ckeditor_upload.urls')),` in your urlpatterns
* Configure CKEditor with: `CKEDITOR.replace('textarea_name', { filebrowserUploadUrl: '/ckeditor_upload/upload/' });`
* OPTIONAL: `CK_FILE_PATH` is path that will be appended to `MEDIA_ROOT` (e.g. `CK_FILE_PATH='uploaded/'`, default is empty string). Make sure to use trailing slash!
