from django.conf.urls import patterns, url

urlpatterns = patterns(
    'serveradmin.dataset.views',
    url(r'^servertypes$', 'servertypes', name='dataset_servertypes'),
    url(r'^servertype/([\w_]+)$', 'view_servertype',
            name='dataset_view_servertype'),
    url(r'^servertype/add/$', 'add_servertype',
            name='dataset_add_servertype'),
    url(r'^servertype/delete/([\w_]+)$', 'delete_servertype',
            name='dataset_delete_servertype'),
    url(r'^servertype/addattr/([\w_]+)$', 'manage_servertype_attr',
            name='dataset_add_servertype_attr'),
    url(r'^servertype/editattr/([\w_]+)/([\w_]+)$', 'manage_servertype_attr',
            name='dataset_edit_servertype_attr'),
    url(r'^servertype/delattr/([\w_]+)/([\w_]+)$', 'delete_servertype_attr',
            name='dataset_delete_servertype_attr'),
    url(r'^attributes$', 'attributes', name='dataset_attributes'),
    url(r'^attributes/delete/([\w_]+)$', 'delete_attribute',
            name='dataset_delete_attribute'),
    url(r'^attributes/add$', 'add_attribute', name='dataset_add_attribute'),
)
