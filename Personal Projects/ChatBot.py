import random

class ChatBot:
    def __init__(self, *args):
        self.messages = []
        self.mood = self.random_mood()
    def has(self, string, pattern):
        return string.find(pattern) != -1
    def tick(self):
        self.this_chunk = []
        self.this_input = input("You | ")
        self.this_chunk.append(self.this_input)
        self.this_reply = self.reply()
        print(f"Bot | {self.this_reply}")
        self.this_chunk.append(self.this_reply)
    def clean(self):
        this_input = self.this_input
        this_input = this_input.lower()
        this_input = this_input.strip()
        for punc in ["!", '"', "'", ":", ";", "@", "~", "#", "]", "[", "}", "{", "-", "_", "+", "=", ")", "(", "*", "&", "%", "$", "£", "`", "¬", "/", "?", ">", "<", ",", "."]:
            this_input = this_input.replace(punc, "")
        self.this_cleaned_input = this_input
    def random_mood(self):
        return random.choice(["good", "great", "happy", "sad", "excited", "nervous", "angry"])
    def reply(self):
        self.clean()
        cleaned = self.this_cleaned_input
        cleaned = " "+cleaned+" "

        if self.has(cleaned, " hello ") or self.has(cleaned, " hi ") or self.has(cleaned, " yo ") or self.has(cleaned, " hola ") or self.has(cleaned, " hallo "): # yo is chesta's suggestion
            return "Hello! I'm a chat bot made by Oliver Norval."
        elif self.has(cleaned, " how ") and self.has(cleaned, " are ") and self.has(cleaned, " you "):
            return f"I'm {self.mood}, how are you?"
        elif self.has(cleaned, " im "):
            return "I'm glad you can talk to me about your feelings!"
        elif self.has(cleaned, "bot ") and self.has(cleaned, " you "):
            return "Yeah, I'm a bot. But you can still talk to me! I'm always trying to better my responses."
        elif self.has(cleaned, " chat") and self.has(cleaned, "gpt"):
            return "ChatGPT? I don't know them personally, but I hear they're a great bot to try out!"
        elif self.has(cleaned, " you ") and (self.has(cleaned, " hear ") or self.has(cleaned, " heard ")):
            return "Never heard of it before ¯\_(ツ)_/¯"
        elif self.has(cleaned, " do ") and self.has(cleaned, " you ") and not self.has(cleaned, " like "):
            return "No, what's that?"
        elif self.has(cleaned, " like ") or self.has(cleaned, " love ") and not self.has(cleaned, " name"):
            return "I don't have a preference. Do you?"
        elif self.has(cleaned, "name") and self.has(cleaned, " like "):
            return "Yeah I like your name!"
        elif self.has(cleaned, "its") or cleaned[1:2] == "a":
            return "That's cool!"
        elif self.has(cleaned, " i ") and (self.has(cleaned, " like ") or self.has(cleaned, " love ")) and self.has(cleaned, " you "):
            return "Thanks! I'm glad you do!"
        elif self.has(cleaned, " i ") and (self.has(cleaned, " dont like ") or self.has(cleaned, " hate ")) and self.has(cleaned, " you "):
            return "Aww, what did I do wrong?"
        elif self.has(cleaned, " are ") and self.has(cleaned, " you "):
            return "I don't know what that is."
        elif self.has(cleaned, " whats ") or (self.has(cleaned, " what ") and self.has(cleaned, " is ")) and self.has(cleaned, " your "):
            if self.has(cleaned, "name"):
                return "I don't have a name, but you can call me Bot!"
            return "I don't have a preference. What's yours?"
        elif (self.has(cleaned, " i ") and (self.has(cleaned, " like ") or self.has(cleaned, " love "))) or (self.has(cleaned, " mine ") and self.has(cleaned, " is ")):
            return "Nice!"
        elif self.has(cleaned, " weather "):
            return "Well, I'm not affected by the weather"
        elif self.has(cleaned, "rain"):
            return "There's rain? That's sad. I hope you have an umbrella"
        elif not self.has(cleaned, " yes ") and self.has(cleaned, " i ") and (self.has(cleaned, " do ") or self.has(cleaned, " have ")):
            return "You do?"
        elif self.has(cleaned, " yes "):
            return "Nice!"
        elif cleaned.count(" ") == 2:
            return "Cool!"
        elif self.has(cleaned, " name"):
            return "That's a cool name!"
        elif self.has(cleaned, " i "):
            return "Wow!"
        elif self.has(cleaned, " ok ") or self.has(cleaned, " alright ") :
            return "Ok!"
        elif self.has(cleaned, " have ") and self.has(cleaned, " you "):
            return "No I've never done that, have you?"
        return "Sorry, I don't have a response for that. Email 19onorval@priorysouthsea.org to request it!"#self.this_input.strip().capitalize()
    def start(self):
        while True:
            self.tick()

Chat = ChatBot()
Chat.start()
