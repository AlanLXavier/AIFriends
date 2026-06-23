import json
import traceback

from django.utils.timezone import now
from langchain_core.messages import SystemMessage, HumanMessage

from web.models.friend import SystemPrompt, Message
from web.views.friend.message.memory.graph import MemoryGraph


def create_system_message():
    system_prompts = SystemPrompt.objects.filter(title='记忆').order_by('order_number')
    prompt = ''
    for sp in system_prompts:
        prompt += sp.prompt
    print(f'=== 记忆模块系统提示词长度: {len(prompt)} ===')
    return SystemMessage(prompt)


def create_human_message(friend):
    prompt = f'【原始记忆】\n{friend.memory}\n'
    prompt += f'【最近对话】\n'
    messages = list(Message.objects.filter(friend=friend).order_by('-id')[:10])
    messages.reverse()
    for m in messages:
        prompt += f'user: {m.user_message}\n'
        prompt += f'ai: {m.output}\n'
    print(f'=== 记忆模块用户消息长度: {len(prompt)}, 包含 {len(messages)} 条最近对话 ===')
    return HumanMessage(prompt)


def update_memory(friend):
    app = MemoryGraph.create_app()

    inputs = {
        'messages': [
            create_system_message(),
            create_human_message(friend),
        ]
    }

    print('=== 记忆模块输入 ===')
    print(json.dumps([m.model_dump() for m in inputs['messages']], ensure_ascii=False, indent=2))

    try:
        res = app.invoke(inputs)
        new_memory = res['messages'][-1].content
        print(f'=== 记忆模块输出 ({len(new_memory)}字符) ===')
        print(new_memory)
        friend.memory = new_memory
        friend.update_time = now()
        friend.save()
    except Exception as e:
        print(f'=== 记忆模块更新失败 ===')
        traceback.print_exc()
