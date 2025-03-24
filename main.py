from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
# import jm2pdf
import os
import pkg.platform.types as platform_types
import jmcomic, os, time, yaml


def download(id):
    # 自定义设置：
    config = "D:\Documents\Workspace\JmPlugin\config.yml"
    loadConfig = jmcomic.JmOption.from_file(config)
    # #如果需要下载，则取消以下注释
    manhua = [id]
    for id in manhua:
        jmcomic.download_album(id,loadConfig)

# 注册插件
@register(name="JM", description="jm", version="0.1", author="RockChinQ")
class MyPlugin(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass

    # 当收到个人消息时触发
    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message  # 这里的 event 即为 PersonNormalMessageReceived 的对象
        sender_id = ctx.event.sender_id
        if msg[:3] == "/jm":  # 如果消息为hello
            id = int(msg[4:])
            # 输出调试信息
            self.ap.logger.debug(f"id{id}")

            # 回复消息 "hello, <发送者id>!"
            # ctx.add_return("reply", [f"id{id}"])
            download(id)
            files_folder = 'D:\Documents\Workspace\JmPlugin\data'
            file_name = f'{id}.png'

            file_path = None
            for file in os.listdir(files_folder):
                if file_name.lower() in file.lower():  # 不区分大小写
                    file_path = os.path.join(files_folder, file)
                    break
            
            # 检查是否找到文件
            if file_path and os.path.exists(file_path):
                try:
                    # 发送文件
                    # await ctx.send_file(sender_id, file_path)
                    file = platform_types.Image(path = file_path)
                    ctx.add_return('reply', file)
                    ctx.add_return("reply", ["文件已发送"])
                except Exception as e:
                    ctx.add_return("reply", ["发送文件时出错：" + str(e)])
            else:
                ctx.add_return("reply", ["未找到匹配的文件"])
            # await ctx.send_file(sender_id, f'D:\Documents\Workspace\JmPlugin\data\{id}.pdf')

            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()

    # 当收到群消息时触发
    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message  # 这里的 event 即为 PersonNormalMessageReceived 的对象
        sender_id = ctx.event.sender_id
        if msg == "hello":  # 如果消息为hello

            # 输出调试信息
            self.ap.logger.debug("hello, {}".format(ctx.event.sender_id))

            # 回复消息 "hello, everyone!"
            ctx.add_return("reply", ["hello, everyone!"])
        elif msg[:3] == "/jm":  # 如果消息为hello
            id = int(msg[4:])
            # 输出调试信息
            self.ap.logger.debug(f"id{id}")

            # 回复消息 "hello, <发送者id>!"
            # ctx.add_return("reply", [f"id{id}"])
            download(id)
            files_folder = 'D:\Documents\Workspace\JmPlugin\data'
            file_name = f'{id}.png'

            file_path = None
            for file in os.listdir(files_folder):
                if file_name.lower() in file.lower():  # 不区分大小写
                    file_path = os.path.join(files_folder, file)
                    break
            
            # 检查是否找到文件
            if file_path and os.path.exists(file_path):
                try:
                    # 发送文件
                    # await ctx.send_file(sender_id, file_path)
                    file = platform_types.Image(path = file_path)
                    ctx.add_return('reply', file)
                    ctx.add_return("reply", ["文件已发送"])
                except Exception as e:
                    ctx.add_return("reply", ["发送文件时出错：" + str(e)])
            else:
                ctx.add_return("reply", ["未找到匹配的文件"])
            # await ctx.send_file(sender_id, f'D:\Documents\Workspace\JmPlugin\data\{id}.pdf')

            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()

    # 插件卸载时触发
    def __del__(self):
        pass
