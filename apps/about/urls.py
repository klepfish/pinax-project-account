from django.conf.urls.defaults import *

urlpatterns = patterns('upload.views',
# (r'^uploader/', 'upload_file'),
    (r'^ipn', 'ipn'),
    (r'^$', 'upload_index'),
)

