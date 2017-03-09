from collections import OrderedDict

from ubuntui.widgets.input import PasswordEditor, StringEditor, YesNo

""" Defining the schema

The schema contains attributes for rendering proper credentials and any
specific provider configurations.

A typical schema is:

'auth-type': 'access-key' - defines the auth type supported by provider
'fields': [] - editable fields in the ui, each field can contain:
  'label' - Friendly label to the user
  'input' - Input widget
  'key'   - key that matches what the provider expects for authentication
  'type'  - 2 types, one being 'auth' and pertains only to credentials, the
            second is 'provider-name' which pertains to items added when
            creating the cloud to use.
"""
aws = {
    'auth-type': 'access-key',
    'fields': [
        {'label': None,
         'input': StringEditor(),
         'key': 'access-key',
         'type': 'auth'},
        {'label': None,
         'input': StringEditor(),
         'key': 'secret-key',
         'type': 'auth'}
    ]
}

maas = {
    'auth-type': 'oauth1',
    'fields': [
        {
            'label': 'server address (only the ip or dns name)',
            'input': StringEditor(),
            'key': 'endpoint',
            'type': 'maas',
        },
        {
            'label': 'api key',
            'input': StringEditor(),
            'key': 'maas-oauth',
            'type': 'auth'
        }
    ]
}

azure = {
    'auth-type': 'service-principal-secret',
    'fields': [
        {
            'label': None,
            'input': StringEditor(),
            'key': 'application-id',
            'type': 'auth'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'subscription-id',
            'type': 'auth'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'tenant-id',
            'type': 'auth'
        },
        {
            'label': None,
            'input': PasswordEditor(),
            'key': 'application-password',
            'type': 'auth'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'storage-account-type',
            'type': 'azure'
        }
    ]
}

google = {
    'auth-type': 'oauth2',
    'fields': [
        {
            'label': None,
            'input': StringEditor(),
            'key': 'private-key',
            'type': 'auth'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'client-id',
            'type': 'auth'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'client-email',
            'type': 'auth'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'project-id',
            'type': 'auth'
        }
    ]
}

cloudsigma = {
    'auth-type': 'userpass',
    'fields': [
        {
            'label': None,
            'input': StringEditor(),
            'key': 'username',
            'type': 'auth'
        },
        {
            'label': None,
            'input': PasswordEditor(),
            'key': 'password',
            'type': 'auth'
        }

    ]
}

joyent = {
    'auth-type': 'userpass',
    'fields': [
        {
            'label': None,
            'input': StringEditor(),
            'key': 'sdc-user',
            'type': 'auth'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'sdc-key-id',
            'type': 'auth'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'private-key',
            'type': 'auth'
        },
        {
            'label': None,
            'input': StringEditor(default='rsa-sha256'),
            'key': 'algorithm',
            'type': 'auth'
        }
    ]
}

openstack = {
    'auth-type': 'userpass',
    'fields': [
        {
            'label': None,
            'input': StringEditor(),
            'key': 'username',
            'type': 'auth'
        },
        {
            'label': None,
            'input': PasswordEditor(),
            'key': 'password',
            'type': 'auth'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'tenant-name',
            'type': 'auth'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'domain-name',
            'type': 'auth'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'project-domain-name',
            'type': 'auth'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'access-key',
            'type': 'auth'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'secret-key',
            'type': 'auth'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'region',
            'type': 'openstack'
        },
        {
            'label': None,
            'input': YesNo(),
            'key': 'use-floating-ip',
            'type': 'openstack'
        },
        {
            'label': None,
            'input': YesNo(),
            'key': 'use-default-secgroup',
            'type': 'openstack'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'network',
            'type': 'openstack'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'external-network',
            'type': 'openstack'
        }
    ]
}

vsphere = {
    'auth-type': 'userpass',
    'fields': [
        {
            'label': 'api-endpoint',
            'input': StringEditor(),
            'key': 'endpoint',
            'type': 'provider'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'user',
            'type': 'auth'
        },
        {
            'label': None,
            'input': PasswordEditor(),
            'key': 'password',
            'type': 'auth'
        },
        {
            'label': None,
            'input': StringEditor(),
            'key': 'external-network',
            'type': 'vsphere'
        },
    ]
}


Schema = [
    ('aws', aws),
    ('aws-china', aws),
    ('aws-gov', aws),
    ('maas', maas),
    ('azure', azure),
    ('azure-china', azure),
    ('google', google),
    ('cloudsigma', cloudsigma),
    ('joyent', joyent),
    ('openstack', openstack),
    ('rackspace', openstack),
    ('vsphere', vsphere)
]


def load_schema(cloud):
    """ Loads a schema
    """
    for s in Schema:
        k, v = s
        if cloud == k:
            return v
    raise Exception("Could not find schema for: {}".format(cloud))


SchemaV1 = OrderedDict([
    ('aws', OrderedDict([
        ('_auth-type', 'access-key'),
        ('access-key', StringEditor()),
        ('secret-key', StringEditor())
    ])),
    ('aws-china', OrderedDict([
        ('_auth-type', 'access-key'),
        ('access-key', StringEditor()),
        ('secret-key', StringEditor())
    ])),
    ('aws-gov', OrderedDict([
        ('_auth-type', 'access-key'),
        ('access-key', StringEditor()),
        ('secret-key', StringEditor())
    ])),
    ('maas', OrderedDict([
        ('_auth-type', 'oauth1'),
        ('@maas-server', StringEditor()),
        ('maas-oauth', StringEditor())
    ])),
    ('azure', OrderedDict([
        ('_auth-type', 'userpass'),
        ('application-id', StringEditor()),
        ('subscription-id', StringEditor()),
        ('tenant-id', StringEditor()),
        ('application-password', PasswordEditor()),
        ('location', StringEditor()),
        ('endpoint', StringEditor()),
        ('storage-endpoint', StringEditor()),
        ('storage-account-type', StringEditor()),
        ('storage-account', StringEditor()),
        ('storage-account-key', StringEditor()),
        ('controller-resource-group', StringEditor())
    ])),
    ('azure-china', OrderedDict([
        ('_auth-type', 'userpass'),
        ('application-id', StringEditor()),
        ('subscription-id', StringEditor()),
        ('tenant-id', StringEditor()),
        ('application-password', PasswordEditor()),
        ('location', StringEditor()),
        ('endpoint', StringEditor()),
        ('storage-endpoint', StringEditor()),
        ('storage-account-type', StringEditor()),
        ('storage-account', StringEditor()),
        ('storage-account-key', StringEditor()),
        ('controller-resource-group', StringEditor())
    ])),
    ('google', OrderedDict([
        ('private-key', StringEditor()),
        ('client-id', StringEditor()),
        ('client-email', StringEditor()),
        ('region', StringEditor()),
        ('project-id', StringEditor()),
        ('image-endpoint', StringEditor())
    ])),
    ('cloudsigma', OrderedDict([
        ('username', StringEditor()),
        ('password', PasswordEditor()),
        ('region', StringEditor()),
        ('endpoint', StringEditor())
    ])),
    ('joyent', OrderedDict([
        ('sdc-user', StringEditor()),
        ('sdc-key-id', StringEditor()),
        ('sdc-url', StringEditor(
            default='https://us-west-1.api.joyentcloud.com')),
        ('private-key-path', StringEditor()),
        ('algorithm', StringEditor(default='rsa-sha256'))
    ])),
    ('openstack', OrderedDict([
        ('_auth-type', 'userpass'),
        ('username', StringEditor()),
        ('password', PasswordEditor()),
        ('tenant-name', StringEditor()),
        ('auth-url', StringEditor()),
        ('auth-mode', StringEditor()),
        ('access-key', StringEditor()),
        ('secret-key', StringEditor()),
        ('region', StringEditor()),
        ('use-floating-ip', YesNo()),
        ('use-default-secgroup', YesNo()),
        ('network', StringEditor())
    ])),
    ('rackspace', OrderedDict([
        ('_auth-type', 'userpass'),
        ('username', StringEditor()),
        ('password', PasswordEditor()),
        ('tenant-name', StringEditor()),
        ('auth-url', StringEditor()),
        ('auth-mode', StringEditor()),
        ('access-key', StringEditor()),
        ('secret-key', StringEditor()),
        ('region', StringEditor()),
        ('use-floating-ip', YesNo()),
        ('use-default-secgroup', YesNo()),
        ('network', StringEditor())
    ])),
    ('vsphere', OrderedDict([
        ('_auth-type', 'userpass'),
        ('host', ("vcenter api-endpoint", StringEditor())),
        ('user', ("vcenter username", StringEditor())),
        ('password', ("vcenter password", PasswordEditor())),
        ('regions', ("datacenter", StringEditor())),
        ('external-network', StringEditor())
    ])),
    ('manual', OrderedDict([
        ('bootstrap-host', StringEditor()),
        ('bootstrap-user', StringEditor()),
        ('use-sshstorage', YesNo())
    ])),
])
