import re
import random

# Простые отражения
reflections = {
    "я": "ты", "мне": "тебе", "ты": "я", "тебя": "меня",
    "моя": "твоя", "твоя": "моя", "моё": "твоё", "твоё": "моё"
}

# Шаблоны и ответы
patterns = [
    (r"привет(.*)", ["Привет! Как я могу помочь?"]),
    (r"как дела", ["У меня всё хорошо. А у тебя?"]),
    (r"(.*)не работает(.*)", ["Что именно не работает? Расскажи подробнее."]),
    (r"я хочу (.*)", ["Почему ты хочешь %1?"]),
    (r"почему (.*)", ["Что думаешь по поводу того, почему %1?"]),
    (r"(.*)", [
        "Расскажи больше.",
        "Интересно… Продолжай, пожалуйста.",
        "Почему ты так считаешь?"
    ])
]

def reflect(fragment: str) -> str:
    tokens = fragment.lower().split()
    return " ".join(reflections.get(w, w) for w in tokens)

def respond(text: str) -> str:
    for pat, responses in patterns:
        m = re.match(pat, text.lower())
        if m:
            resp = random.choice(responses)
            if "%1" in resp and m.groups():
                return resp.replace("%1", reflect(m.group(1)))
            return resp
    return "Я тебя не понимаю."
