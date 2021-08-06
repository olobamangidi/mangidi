#simple but brittle 
************************************************
#add ansible as higher level tool

from fabric import Application

def provisioning():
  api.sudo('apt-get install python python-dev python-pip')
  api.sudo('pip install virtualenv')
  api.run('git clone git@host:group/app')
  api.run('virtualen  --no-site-packages  /app/env')


def config():
  api.put('startup.sh', 'startup.sh')
  api.sudo('mv startup.sh /etc/init.d/app')
  api.put('app-config.ini' 'app/config.ini')

def deploy():
  api.run('git -C /app/pull')
  api.run('source app/env/bin/activate' && \
    'pip install -U -r requirements')
  api.sudo('service app start')
