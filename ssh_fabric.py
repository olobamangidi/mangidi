#AUTOMATE WEBDEPLOYMENT WITH FABRIC 
################################

from fabric.api import env, run  

env.hosts = ['192.130.41.204', '192.170.41.214', '192.190.1.244']

def update():
  run('uptime')

  # run it 
  fab -P uptime 
  fab --list 
