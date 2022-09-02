# JoinTitle
>当玩家加入服务器时自动运行/title命令  
## 配置文件  
可以结合 **[/title命令语法](https://minecraft.fandom.com/zh/wiki/%E5%91%BD%E4%BB%A4/title)** 和 **[Minecraft格式化代码](https://minecraft.fandom.com/zh/wiki/%E6%A0%BC%E5%BC%8F%E5%8C%96%E4%BB%A3%E7%A0%81)** 来编辑此文件  

`config/join_title/jointitle.json`
```
{
    'title' : '§l§f欢迎回到§a服务器', 
    'subtitle' : '',
    'actionbar' : '',
    'permissions' : {
        'title' : 0,    #!!title命令的权限(WIP)
        'set' : 3   #!!title set命令的权限(WIP)
    }
}
```
***
## 更新前瞻
>指令配置  
自动播放播放指定音效