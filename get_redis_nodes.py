from kazoo.client import KazooClient
from kazoo.client import KazooState

def my_listener(state):
    if state == KazooState.LOST:
        print("LOST")
    elif state == KazooState.SUSPENDED:
        print("SUSPENDED")
    else:
        print(state)

zk = KazooClient(hosts='127.0.0.1:2181')
#zk.add_listener(my_listener)    

zk.start()
#zk.ensure_path("/workers111")

if zk.exists('/workers'):
    print('/workers znode exists')

sum = 0

@zk.ChildrenWatch("/workers/redis")
def watch_children(children):
    print("Children are now: %s" % children)
    for child in children:
        print(child)
# Above function called immediately, and from then on

@zk.DataWatch("/workers/redis")
def watch_node(data, stat):
    print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))


while True:
    sum += 1

zk.stop()

