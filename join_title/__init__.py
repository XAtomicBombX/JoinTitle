from mcdreforged.api.all import *

config = {
    'title': '§l§f欢迎回到§a服务器',
    'subtitle': '',
    'actionbar': '',
    'permissions': {
        'title': 0,
        'set': 3
    }
}


def show_title(server: ServerInterface, player, title, subtitle, actionbar):
    server.execute(f'title {player} title "{title}"')

    if subtitle:
        server.execute(f'title {player} subtitle "{subtitle}"')

    if actionbar:
        server.execute(f'title {player} actionbar "{actionbar}"')


def load_config(server: ServerInterface):
    psi = server.as_plugin_server_interface()
    global config
    config = psi.load_config_simple("jointitle.json",
                                    default_config=config)


def on_player_joined(server: ServerInterface, player, info):
    show_title(server, player, config['title'], config['subtitle'],
               config['actionbar'])


def write_config(source:CommandSource,obj, string):
    """
    写入字典 config
    :param obj: 写入字典 default_config的键
    :param string: 写入字典 default_config的值
    :return: None
    """
    server = source.get_server()
    psi = server.as_plugin_server_interface()
    global config
    config[obj] = string
    psi.save_config_simple(config,"jointitle.json")
    return None


def register_command(server:PluginServerInterface):
    """
    实现以下指令
    !!title [set] [title|subtitle|actionbar] [string:input_message]
    :return: None
    """
    server.register_command(
        Literal('!!title'). \
            then(
            Literal('set').
            then(
                Literal("title").
                then(
                    GreedyText("input_message").
                    runs(lambda src,ctx:write_config(src,'title',ctx["input_message"]))
                )
            ). \
            then(
                Literal("subtitle").then(
                    GreedyText("input_message").
                    runs(lambda src,ctx:write_config(src,'subtitle',ctx["input_message"]))
                )
            ). \
            then(
                Literal("actionbar").then(
                    GreedyText("input_message").
                    runs(lambda src,ctx:write_config(src,'actionbar',ctx["input_message"])
                    )
                )
            )
        )
    )


def on_load(server: ServerInterface, old):
    # show_title(server,'@a','JoinTitle已加载',None,None)
    psi = server.as_plugin_server_interface()
    load_config(server)
    register_command(psi)
