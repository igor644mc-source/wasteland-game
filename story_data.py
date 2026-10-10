# story_data.py

STORY = {
    "start": {
        "text": "Ты пришёл в себя в полуразрушенном бункере. В воздухе пахнет гарью. Голова трещит, но сирена тревоги уже умолкла. На столе лежит ржавый фомка и фляга с водой.",
        "image": "bunker_start",
        "choices": [
            {
                "text": "Забрать флягу и фомку (+20 Вода, +Оружие)",
                "next_node": "take_supplies",
                "effects": {"water": +20, "health": 0}
            },
            {
                "text": "Сразу бежать к выходу из бункера",
                "next_node": "bunker_exit",
                "effects": {"water": 0, "health": -5}
            }
        ]
    },
    "take_supplies": {
        "text": "Ты забрал припасы. По крайней мере, жажда тебе пока не грозит. Подойдя к тяжёлой гермодвери, ты слышишь за ней странный шорох...",
        "image": "bunker_door",
        "choices": [
            {
                "text": "Приготовиться к бою и открыть дверь",
                "next_node": "fight_mutant",
                "effects": {"health": -10}
            },
            {
                "text": "Попробовать найти другой выход через вентиляцию",
                "next_node": "ventilation",
                "effects": {"water": -5}
            }
        ]
    },
    # Дополнительные развилки добавляются сюда...
}

def get_node(node_id):
    return STORY.get(node_id, STORY["start"])
