from mcdreforged.api.all import *

default_config = {
    'title' : '§l§f欢迎回到§a服务器',
    'subtitle' : '',
    'actionbar' : '',
    'permissions' : {
        'title' : 0,
        'set' : 3
    }
}

def load_config(server:PluginServerInterface):
    global config
    config = server.load_config_simple("jointitle.json",default_config=default_config)


def on_player_join(server):
    pass

def on_load(server:PluginServerInterface,old):
    load_config(server)

