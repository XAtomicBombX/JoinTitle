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

def show_title(server:ServerInterface,player,title,subtitle,actionbar):
    server.execute(f'title {player} title "{title}"')
    
    if subtitle:
        server.execute(f'title {player} subtitle "{subtitle}"')
    
    if actionbar:
        server.execute(f'title {player} actionbar "{actionbar}"')

def load_config(server:ServerInterface):
    psi = server.as_plugin_server_interface()
    global config
    config = psi.load_config_simple("jointitle.json",default_config=default_config)

def on_player_joined(server:ServerInterface,player,info):
    show_title(server,player,config['title'],config['subtitle'],config['actionbar'])

def on_load(server:ServerInterface,old):
    # show_title(server,'@a','JoinTitle已加载',None,None)
    load_config(server)
