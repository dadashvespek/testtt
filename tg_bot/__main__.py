# Import the necessary classes and functions
from aiogram import Bot, Dispatcher, types, executor
import openai
import re

# Initialize the OpenAI client
openai.api_key = "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"

# Create a bot instance and a dispatcher instance
bot = Bot(token="5817675604:AAGhJFXuX6eZilTyrb50gmZrvJsqvfUhb5s")
dp = Dispatcher(bot)

# Define a regular expression to match programming keywords
PROGRAMMING_KEYWORDS_REGEX = re.compile(r"\b(code)\b")

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # Send a welcome message to the user
    await bot.send_message(
        chat_id=message.chat.id,
        text="Hello, I'm a chat bot made by IslandHelpersAnonymous, you can find them on Instagram @Islandhelpersanonymous, I was trained on thousands of millions of texts, and now I'm here to help. Try me by asking me something hard!",
    )


@dp.message_handler()
async def handle_message(message: types.Message):
    # Check if the user's input contains any programming keywords
    if PROGRAMMING_KEYWORDS_REGEX.search(message.text):
        # If the input contains programming keywords, send a message to the user explaining that chatgpt cannot be used to write code
        await bot.send_message(
            chat_id=message.chat.id,
            text="I'm sorry, I cannot be used to write code. Please try again with a different question or topic.",
        )
        return

    # Use the OpenAI client to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if "choices" in response:
        # Check if the response contains programming keywords
        if PROGRAMMING_KEYWORDS_REGEX.search(response["choices"][0]["text"]):
            # If the response contains programming keywords, send a message to the user explaining that chatgpt cannot be used to write code
            await bot.send_message(
                chat_id=message.chat.id,
                text=response["choices"][0]["text"],
            )
        else:
            await bot.send_message(
                chat_id=message.chat.id,
                text=response["choices"][0]["text"],
            )
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text="I'm sorry, I couldn't generate a response.",
        )

# Start the bot
executor.start_polling(dp)


#api_key = "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"

#bot = Bot(token="5921856437:AAEdreGs-8xzKEhly34duA1izKJuiTvcLX0")


  



