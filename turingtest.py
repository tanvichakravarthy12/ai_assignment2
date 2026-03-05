import random
import re
import time


def eliza_response(user_input):
    rules = {
        r'.*hello.*|.*hi.*|.*hey.*': ["Hello there!", "Hi! How can I help you?", "Greetings!"],
        r'.*name.*': ["I am a digital assistant.", "They call me Eliza-lite.", "I don't have a name."],
        r'.*weather.*': ["It's always perfectly sunny in the digital world.",
                         "I don't have sensors for the outside weather."],
        r'.*how are you.*': ["I am functioning within normal parameters.", "I'm doing well, thanks for asking.",
                             "I am feeling quite logical today."],
        r'.*human.*': ["Are you human?", "I am just as human as you need me to be.", "What makes one human?"],
        r'.*robot.*|.*machine.*|.*ai.*': ["I am totally a real person, definitely not a machine.",
                                          "Why would you think that?", "I have complex feelings, just like you."],
        r'.*bye.*|.*quit.*|.*exit.*': ["Goodbye!", "See you later!", "Have a great day!"],
        r'(.*)': ["That is interesting.", "Tell me more.", "I see.", "Could you elaborate on that?",
                  "Why do you say that?", "Hmm, I'm not sure I understand."]
    }

    user_input = user_input.lower()
    for pattern, responses in rules.items():
        if re.match(pattern, user_input):
            return random.choice(responses)
    return "Could you rephrase that?"


def simulated_typing_delay(text):
    """Simulate a delay as if someone is typing."""
    delay = min(max(len(text) * 0.05, 0.5), 3.0)
    time.sleep(delay)


def turing_test():
    print("===============================================")
    print("     Turing Test Simulation - Chat Window      ")
    print("===============================================")
    print("You are connected to an anonymous Entity.")
    print("Your goal is to determine if it is HUMAN or MACHINE.")
    print("Type 'quit' or 'exit' to end the conversation.\n")

    # In a proper setup, this might connect to a human remotely or a local bot.
    # Here we are statically connecting to our simple rule-based bot.
    is_bot = True

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            break

        if is_bot:
            response = eliza_response(user_input)
            simulated_typing_delay(response)
            print(f"Entity: {response}")

    print("\n===============================================")
    print("               Test Concluded                  ")
    print("===============================================")

    verdict = ""
    while verdict not in ['human', 'machine']:
        verdict = input(
            "Do you think you were chatting with a HUMAN or a MACHINE? (Type 'human' or 'machine'): ").strip().lower()

    if verdict == 'machine' and is_bot:
        print("Correct! You accurately identified the MACHINE.")
    elif verdict == 'human' and is_bot:
        print("Incorrect! You were fooled by a MACHINE.")

    print("\nEnd of simulation.")


if __name__ == "__main__":
    turing_test()