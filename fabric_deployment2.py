#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#deploy with fabric 

# vi fabfile.py

from fabric.api import *

# the user to use for the remote commands
env.user = 'appuser'
# the servers where the commands are executed
env.hosts = ['server1.example.com', 'server2.example.com']

def pack():
    # build the package
    local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
    # figure out the package name and version
    dist = local('python setup.py --fullname', capture=True).strip()
    filename = f'{dist}.tar.gz'

    # upload the package to the temporary folder on the server
    put(f'dist/{filename}', f'/tmp/{filename}')

    # install the package in the application's virtualenv with pip
    run(f'/var/www/yourapplication/env/bin/pip install /tmp/{filename}')

    # remove the uploaded package
    run(f'rm -r /tmp/{filename}')

    # touch the .wsgi file to trigger a reload in mod_wsgi
    run('touch /var/www/yourapplication.wsgi')

Running Fabfiles

$ fab pack deploy



def free_space(g):
     return g.run("df -h")

free_space(group)


