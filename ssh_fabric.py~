############################################################
from fabtic import SerialGroup 


#192.168.41.130
#192.168.41.128
#group = SerialGroup("manunited1", "manunited2", user = "meme", connect_kwargs = {"password":"ansible"})
group = SerialGroup("198.168.41.328", "198.168.41.320", user = "meme", connect_kwargs = {"password":"ansile"})

#execute 
group.run("df -hT")
# hide result from the console 
result = group.run("df -hT", hide = True) 



def free_space(g):
     return g.run("df -h")

free_space(group)

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# responding to sudo passwords 

from  invoke import Responder 
from fabric import Connection  


#group = SerialGroup("198.168.41.328", "198.168.41.328", user = "meme", connect_kwargs = {"password":"!ansible!"})
group = Connection("meme@198.168.41.328", connect_kwargs = {"password":"!ansible!"})
sudopass = Responder(pattern = r"\[sudo\] password for meme: ", response = "!ansible!\n")
#watchers allow you to specify a list of functions 
group.run("sudo whoami", pty = True, watchers = [sudopass])




C = Connection("meme@182.168.41.330", connect_kwargs = {"password":"!ansible!"})
sudopass = Responder(pattern = r"\[sudo\] password for meme: ", response = "!ansible!\n")
result = C.run("sudo whoami", pty = True, watchers = [sudopass])
#<Result cmd='sudo whoami' exited=0>

type(result)
dir(result)



#AUTOMATE WEBDEPLOYMENT WITH FABRIC 
################################

from fabric.api import env, run  

env.hosts = ['192.130.41.204', '192.170.41.214', '192.190.1.244']

def update():
  run('uptime')

  # run it 
  fab -P uptime 
  fab --list 

  
  def uptime():
     C.run('uptime')

>>> uptime()
 10:09:09 up  9:39,  2 users,  load average: 2.34, 2.61, 2.61

  
  def free_space(g):
...     return g.run("df -h")
...
>>> free_space(group)
Filesystem               Size  Used Avail Use% Mounted on
devtmpfs                 475M     0  475M   0% /dev
tmpfs                    487M     0  487M   0% /dev/shm
  
  
  
  
  
  
  
  
