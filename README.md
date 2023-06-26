
## Discord Bot

Welcome to the Discord OpenAI Bot, a powerful bot designed to provide intelligent responses and entertainment within your Discord server. This bot leverages the OpenAI API to enable seamless question-answering capabilities using natural language processing. Get ready to have your questions answered and enjoy some lighthearted humor with additional commands!

The Discord OpenAI Bot is designed to enhance your Discord server with intelligent question-answering capabilities and fun-filled moments. It serves as a valuable resource for knowledge sharing and light-hearted amusement. Whether you have burning questions or simply want to enjoy some quality humor, this bot has you covered.

**Note:** This program runs on an older version of discord.py, therefore if you do not are not using Discord.py 1.7.3, the program may not work. Also, some APIs may have expired from API deactivation. Furthermore, you must use you're own discord bot TOKEN and OpenAI API token in order to apply this program to your bot.

Feel free to explore the codebase, customize the bot's responses, or add additional commands to further expand its functionality. If you have any questions or suggestions, please don't hesitate to reach out. Get ready to elevate your Discord server experience with the power of OpenAI and engaging bot commands!

## Tech Stack

**Language** Python

**Libraries:** Discord.py

**APIs:** OpenAI API, Official Joke API, TheCatAPI, Dog.ceo, Meme-api

**Client:** Discord

**Server:** Replit


## Features

**!ask Command:** With the !ask command, you can ask the bot any question that comes to mind. Utilizing the power of the OpenAI API, the bot intelligently processes your question and provides a relevant response. Whether you're seeking factual information, trivia, or general knowledge, the bot is here to assist and engage in insightful conversations.

**!joke Command:** Need a good laugh? The !joke command is at your service. With a simple command, the bot will share a delightful, humorous joke to brighten up your Discord server. Sit back, relax, and let the bot deliver the comedic relief.

**!meme Command:** The !meme command will generate a random meme after the bot pings the Meme-api. After the meme is pulled, the bot will send the meme in the discord server.

**!cat Command:** Similar to the !meme command, the !cat command will receive and send a random picture of the cat using TheCatAPI. The bot communicates with TheCatAPI in order to generate this image.

**!poll Command:** The !poll command will take a question and an option of answers to display. An example use of this command is "!ask question option1 option2." This will result in the bot sending the question with each option having a different emote reaction to represent a vote. Users can vote and the option with the most upvotes wins.

**!say Command:** The !say command will take in a text phrase entered by the user and repeat the text sent back to all server members with a text-to-speech voice. 

**!userinfo Command:** The !userinfo command will take in a username as an argument and return information about the user such as when they joined the server, their role, and more.

**!serverinfo Command:** The !serverinfo command will display information about the server to users through a message. This command will display information such as when the server was created, how many members it has, and more.

**!help Command:** The help command will display all of the available commands that the users can use and what all the commands do.

**Customizable and Extensible:** The bot's codebase is designed to be easily customizable and extensible. You can modify the command prefixes, add additional commands, or enhance existing functionalities to tailor the bot to your specific needs and preferences.

**User-Friendly Interface:** The bot provides a user-friendly interface, ensuring a seamless experience for both server administrators and regular users. Clear and concise command usage instructions make it easy for everyone to interact with the bot and enjoy its features.

**OpenAI Integration:** By incorporating the OpenAI API, this bot benefits from advanced natural language processing capabilities, ensuring accurate and relevant responses. It opens up possibilities for diverse use cases, from educational and informative interactions to engaging discussions


## API Reference

```
  OpenAI API
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **(Private)** OpenAI Key |


The OpenAI key is private due to the cost to run the API.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`TOKEN`

The token is used to connect your bot to the code that you write. Each bot has a unique token, so use the token that pertains to your bot.


## FAQ

#### How can I get the token key to access OpenAI's API

In order to get the token key to access OpenAI's API, you have to go to OpenAI's website and create an account to sign up to receive a key.

#### Some commands don't work with the bot. How can I fix them?

Some of the bot's functions may be outdated due to discord changing their discord.py library functions and requirements. Please check the version of discord.py that you are running.

![Logo](https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/91_Discord_logo_logos-512.png)

![Logo](https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png)
