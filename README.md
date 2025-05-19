# 🔍 CheckBan Free Fire Discord Bot

![Status](https://img.shields.io/badge/status-active-brightgreen)

A Discord bot to check if a Free Fire account is banned, using a user ID. Also includes a Flask-based status server.

- [Features](#-features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Create a Discord Bot](#create-a-discord-bot)
- [Technologies Used](#technologies-used)
- [License](#license)
- [Author](#author)

## 🚀 Features

- Check if a Free Fire account is banned using the `!ID <user_id>` command.
- Returns ban status and ban duration (if available) in an embedded Discord message.
- Flask web server on `http://localhost:10000` to indicate bot status.
- Secure credentials using `.env`.

## Requirements

- Python 3.8+
- A Discord bot token
- A `.env` file containing:
  ```ini
  TOKEN=your_bot_token
  ```

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/paulafredo/check-ban-and-info-discord
   cd your-repo
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```



4. Create a `.env` file in the root directory and add your credentials:
   ```ini
   TOKEN=your_bot_token
   ```

5. Run the bot:
   ```sh
   python main.py
   ```

## 📸 Demo

<div align="center">
  <img src="https://github.com/user-attachments/assets/bbcae61d-72a7-4caf-9d3e-cc587546a06b" alt="demo 1" width="400"/>
  <img src="https://github.com/user-attachments/assets/5c9168a0-3f5a-46e3-af1f-8f6fe31cbae3" alt="demo 2" width="410"/>
</div>

> 🎥 The Git in this demo was provided by [NinjaHex]() – 


## Usage

- Use `!ID <user_id>` in a Discord server where the bot is present.
- The bot will fetch ban information from [api-check-ban-freefire](https://github.com/paulafredo/api-check-ban-freefire) and respond with an embedded message.
- The bot's status can be checked via the Flask server running at `http://localhost:10000`.



## 🛠️ Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **"New Application"**, and give your bot a name.
3. In the left sidebar, go to the **"Bot"** section and click **"Add Bot"**, then confirm with **"Yes, do it!"**.
4. Under the **Token** section, click **"Reset Token"** or **"Copy"** to get your `TOKEN`.
5. Go to **"General Information"** and copy the `APPLICATION_ID`.
6. Paste both values into your `.env` file:
      ```ini
   APPLICATION_ID=your_application_id
   TOKEN=your_bot_token
   ```


## 🔗 Invite the Bot to a Discord Server

1. Go to **OAuth2 > URL Generator** in the Developer Portal.
2. Under **Scopes**, check:
   - `bot`
   - `applications.commands`
3. Under **Bot Permissions**, check at least:
   - `Send Messages`
   - `Embed Links`
4. Copy the generated URL and open it in your browser to invite the bot to your server.


## 📚 Bot Commands

### `!ID <user_id>`
Check whether a Free Fire account is **banned** or **not**.

- 📥 **Input:** a user ID (UID)
- 📤 **Output:** an embedded message with the account status (banned or not)
- ✅ **Example:**

---

---
### `!lang <language_code>`
Change the **display language** of the bot for the current user.

- 🌐 **Available languages:**
- `en` – English (default)
- `fr` – French

- ✅ **Examples:**
   - `!lang en`
   - `!lang fr`
     
> ℹ️ By default, the language is set to **English (`en`)** if no other language is selected.


### 🤖 Invite the Bot to Your Server

Click the link below to invite the CheckBan bot to your Discord server:

👉 [**Add CheckBan to Your Server**](https://discord.com/oauth2/authorize?client_id=1332414680928485457&permissions=274877975552&scope=bot+applications.commands)


## Technologies Used

- Python
- Discord.py
- Flask
- dotenv

## License

This project is licensed under the MIT License. Feel free to use and modify it.

## Author

[Paul Alfredo](https://github.com/paulafredo)

