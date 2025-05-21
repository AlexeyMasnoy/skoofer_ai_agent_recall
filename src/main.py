from agent import MCPClient
from eliza_bot import respond as eliza_respond

def main():
    client = MCPClient()
    print("Eliza-Agent запущен. Пиши 'status' для статуса, 'trade' для сделки, 'exit' чтобы выйти.")
    while True:
        text = input("> ").strip().lower()
        if not text:
            continue
        if text == "exit":
            print("Пока!")
            break
        elif text == "status":
            status = client.get_competition_status()
            print("Статус соревнования:", status)
        elif text == "trade":
            quote = client.get_quote("USDC", "SOL", 10)
            print("Котировка:", quote)
            trade = client.execute_trade("USDC", "SOL", 10, reasoning="Пример сделки через Eliza-Agent")
            print("Результат сделки:", trade)
        else:
            # всё остальное – диалог с ELIZA
            print(eliza_respond(text))

if __name__ == "__main__":
    main()
