from pyrogram import filters
from devgagan import app
from config import OWNER_ID
from devgagan.core.func import subscribe
import asyncio
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.raw.functions.bots import SetBotInfo
from pyrogram.raw.types import InputUserSelf
# ------------------- Start-Buttons ------------------- #

from pyrogram.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
# Set bot commands in one place
@app.on_message(filters.command("set"))
async def set(_, message):
    if message.from_user.id not in OWNER_ID:
        await message.reply("You are not authorized to use this command.")
        return
    # Setting all the bot commands
    await app.set_bot_commands([
        BotCommand("start", "🚀 Start the bot"),
        BotCommand("batch", "🫠 Extract in bulk"),
        BotCommand("login", "🔑 Get into the bot"),
        BotCommand("logout", "🚪 Get out of the bot"),
        BotCommand("token", "🎲 Get 3 hours free access"),
        BotCommand("adl", "👻 Download audio from 30+ sites"),
        BotCommand("dl", "💀 Download videos from 30+ sites"),
        BotCommand("transfer", "💘 Gift premium to others"),
        BotCommand("myplan", "⌛ Get your plan details"),
        BotCommand("add", "➕ Add user to premium"),
        BotCommand("rem", "➖ Remove from premium"),
        BotCommand("settings", "⚙️ Personalize things"),
        BotCommand("stats", "📊 Get stats of the bot"),
        BotCommand("plan", "🗓️ Check our premium plans"),
        BotCommand("terms", "🥺 Terms and conditions"),
        BotCommand("speedtest", "🚅 Speed of server"),
        BotCommand("get", "🗄️ Get all user IDs"),
        BotCommand("lock", "🔒 Protect channel from extraction"),
        BotCommand("gcast", "⚡ Broadcast message to bot users"),
        BotCommand("help", "❓ If you're a noob, still!"),
        BotCommand("cancel", "🚫 Cancel batch process")
    ])
    
    await message.reply("✅ Commands configured successfully!")

# Function to split and manage the help message in multiple parts

# Function to split and manage the help message in multiple parts
help_pages = [
    (
        "📝 **Bot Commands Overview (1/2)**:\n\n"
        "1. **/add userID**\n"
        "> Add user to premium (Owner only)\n\n"
        "2. **/rem userID**\n"
        "> Remove user from premium (Owner only)\n\n"
        "3. **/transfer userID**\n"
        "> Transfer premium to your beloved major purpose for resellers (Premium members only)\n\n"
        "4. **/get**\n"
        "> Get all user IDs (Owner only)\n\n"
        "5. **/lock**\n"
        "> Lock channel from extraction (Owner only)\n\n"
        "6. **/dl link**\n"
        "> Download videos (Not available in v3 if you are using)\n\n"
        "7. **/adl link**\n"
        "> Download audio (Not available in v3 if you are using)\n\n"
        "8. **/login**\n"
        "> Log into the bot for private channel access\n\n"
        "9. **/batch**\n"
        "> Bulk extraction for posts (After login)\n\n"
    ),
    (
        "📝 **Bot Commands Overview (2/2)**:\n\n"
        "10. **/logout**\n"
        "> Logout from the bot\n\n"
        "11. **/stats**\n"
        "> Get bot stats\n\n"
        "12. **/plan**\n"
        "> Check premium plans\n\n"
        "13. **/speedtest**\n"
        "> Test the server speed (not available in v3)\n\n"
        "14. **/terms**\n"
        "> Terms and conditions\n\n"
        "15. **/cancel**\n"
        "> Cancel ongoing batch process\n\n"
        "16. **/myplan**\n"
        "> Get details about your plans\n\n"
        "17. **/session**\n"
        "> Generate Pyrogram V2 session\n\n"
        "18. **/settings**\n"
        "> 1. SETCHATID : To directly upload in channel or group or user's dm use it with -100[chatID]\n"
        "> 2. SETRENAME : To add custom rename tag or username of your channels\n"
        "> 3. CAPTION : To add custom caption\n"
        "> 4. REPLACEWORDS : Can be used for words in deleted set via REMOVE WORDS\n"
        "> 5. RESET : To set the things back to default\n\n"
        "> You can set CUSTOM THUMBNAIL, PDF WATERMARK, VIDEO WATERMARK, SESSION-based login, etc. from settings\n\n"
        "**__Powered by @Spark_Developer__**"
    )
]

# Helper function to send or edit help messages with navigation buttons
async def send_or_edit_help_page(_, message, page_number):
    if page_number < 0 or page_number >= len(help_pages):
        return

    # Define the navigation buttons (previous, next)
    prev_button = InlineKeyboardButton("◀️ Previous", callback_data=f"help_prev_{page_number}")
    next_button = InlineKeyboardButton("Next ▶️", callback_data=f"help_next_{page_number}")

    # Add buttons conditionally
    buttons = []
    if page_number > 0:
        buttons.append(prev_button)
    if page_number < len(help_pages) - 1:
        buttons.append(next_button)

    # Create the keyboard
    keyboard = InlineKeyboardMarkup([buttons])

    # Delete the previous message before sending a new one
    await message.delete()

    # Send the appropriate help page
    await message.reply(
        help_pages[page_number],
        reply_markup=keyboard
    )

# Start command with help navigation
@app.on_message(filters.command("help"))
async def help(client, message):
    join = await subscribe(client, message)
    if join == 1:
        return
    
    # Show the first help page
    await send_or_edit_help_page(client, message, 0)

# Handle callback queries for help navigation
@app.on_callback_query(filters.regex(r"help_(prev|next)_(\d+)"))
async def on_help_navigation(client, callback_query):
    action, page_number = callback_query.data.split("_")[1], int(callback_query.data.split("_")[2])

    if action == "prev":
        page_number -= 1
    elif action == "next":
        page_number += 1

    # Edit the appropriate help page
    await send_or_edit_help_page(client, callback_query.message, page_number)

    # Acknowledge the callback query
    await callback_query.answer()


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@app.on_message(filters.command("terms") & filters.private)
async def terms(client, message):
    terms_text = (
        "📜 **Terms and Conditions** 📜\n\n"
        "✨ We are not responsible for user deeds, and we do not promote copyrighted content. If any user engages in such activities, it is solely their responsibility.\n"
        "✨ Upon purchase, we do not guarantee the uptime, downtime, or the validity of the plan. __Authorization and banning of users are at our discretion; we reserve the right to ban or authorize users at any time.__\n"
        "✨ Payment to us **__does not guarantee__** authorization for the /batch command. All decisions regarding authorization are made at our discretion and mood.\n"
    )
    # Buttons for "See Plans" and "Contact"
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📋 See Plans", callback_data="see_plan")],
            [InlineKeyboardButton("💬 Contact Now", url="https://t.me/Spark_Developer")],
        ]
    )
    await message.reply_text(terms_text, reply_markup=buttons)


@app.on_message(filters.command("plan") & filters.private)
async def plan(client, message):
    plan_text = (
    """    - ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴ𝒔 - 

- 120ʀ𝒔 - 1 ᴡᴇᴇᴋ
- 300ʀ𝒔 - 1 ᴍᴏɴᴛʜ𝒔
- 800ʀ𝒔 - 3 ᴍᴏɴᴛʜ𝒔
(𝑡𝑒𝑟𝑚𝑠 𝑎𝑛𝑑 𝑐𝑜𝑛𝑑𝑖𝑡𝑖𝑜𝑛𝑠 𝑎𝑝𝑝𝑙𝑦).

💗 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇ𝒔 💗

○ 𝐵𝑎𝑡𝑐ℎ 𝑈𝑝𝑡𝑜 100𝑘 𝑓𝑖𝑙𝑒𝑠 𝐴𝑡 𝑂𝑛𝑐𝑒.
○ 𝐶𝑢𝑠𝑡𝑜𝑚 𝐶𝑎𝑝𝑡𝑖𝑜𝑛 𝑆𝑢𝑝𝑝𝑜𝑟𝑡.
○𝑆𝑒𝑡 𝑅𝑒𝑛𝑎𝑚𝑒 𝑇𝑎𝑔.
○ 𝑅𝑒𝑚𝑜𝑣𝑒 𝑆𝑝𝑒𝑐𝑖𝑓𝑖𝑐 𝑊𝑜𝑟𝑑𝑠 𝐹𝑟𝑜𝑚 𝐶𝑎𝑝𝑡𝑖𝑜𝑛.
○ 𝑼𝒑𝒍𝒐𝒂𝒅 𝑫𝒊𝒓𝒆𝒄𝒕𝒍𝒚 𝑰𝒏 𝒀𝒐𝒖𝒓 𝑪𝒉𝒂𝒏𝒏𝒆𝒍.
○ 𝑼𝒍𝒕𝒓𝒂 𝑭𝒂𝒔𝒕 𝑺𝒑𝒆𝒆𝒅 😁 
○ ʜɪɢʜ-𝒔ᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ & 𝑼𝒑𝒍𝒐𝒂𝒅
○ 𝑨𝒍𝒍 𝑳𝒊𝒏𝒌𝒔 𝑺𝒖𝒑𝒑𝒐𝒓𝒕𝒆𝒅.
○ 𝑷𝒆𝒓𝒎𝒂𝒏𝒆𝒏𝒕  𝑻𝒉𝒖𝒎𝒃𝒏𝒂𝒊𝒍 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 
○ ꜰᴜʟʟ ᴀᴅᴍɪɴ 𝒔ᴜᴘᴘᴏʀᴛ

✨𝑭𝒐𝒓 ᴜᴘɪ ɪᴅ 𝒐𝒓 𝑸𝑹
 𝑫𝒎 : @Spark_Developer

📜 𝑇𝑒𝑟𝑚𝑠 𝑎𝑛𝑑 𝐶𝑜𝑛𝑑𝑖𝑡𝑖𝑜𝑛𝑠: 𝐹𝑜𝑟 𝑓𝑢𝑟𝑡ℎ𝑒𝑟 𝑑𝑒𝑡𝑎𝑖𝑙𝑠 𝑎𝑛𝑑 𝑐𝑜𝑚𝑝𝑙𝑒𝑡𝑒 𝑡𝑒𝑟𝑚𝑠 𝑎𝑛𝑑 𝑐𝑜𝑛𝑑𝑖𝑡𝑖𝑜𝑛𝑠, 𝑝𝑙𝑒𝑎𝑠𝑒 𝑠𝑒𝑛𝑑 /terms.

ᴄʟɪᴄᴋ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /myplan """
)
    # Buttons for "See Terms" and "Contact"
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📜 See Terms", callback_data="see_terms")],
            [InlineKeyboardButton("💬 Contact Now", url="https://t.me/Spark_Developer")],
        ]
    )
    await message.reply_text(plan_text, reply_markup=buttons)


@app.on_callback_query(filters.regex("see_plan"))
async def see_plan(client, callback_query):
    plan_text = (
  """     - ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴ𝒔 - 

- 120ʀ𝒔 - 1 ᴡᴇᴇᴋ
- 300ʀ𝒔 - 1 ᴍᴏɴᴛʜ𝒔
- 800ʀ𝒔 - 3 ᴍᴏɴᴛʜ𝒔
(𝑡𝑒𝑟𝑚𝑠 𝑎𝑛𝑑 𝑐𝑜𝑛𝑑𝑖𝑡𝑖𝑜𝑛𝑠 𝑎𝑝𝑝𝑙𝑦).

💗 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇ𝒔 💗

○ 𝐵𝑎𝑡𝑐ℎ 𝑈𝑝𝑡𝑜 100𝑘 𝑓𝑖𝑙𝑒𝑠 𝐴𝑡 𝑂𝑛𝑐𝑒.
○ 𝐶𝑢𝑠𝑡𝑜𝑚 𝐶𝑎𝑝𝑡𝑖𝑜𝑛 𝑆𝑢𝑝𝑝𝑜𝑟𝑡.
○𝑆𝑒𝑡 𝑅𝑒𝑛𝑎𝑚𝑒 𝑇𝑎𝑔.
○ 𝑅𝑒𝑚𝑜𝑣𝑒 𝑆𝑝𝑒𝑐𝑖𝑓𝑖𝑐 𝑊𝑜𝑟𝑑𝑠 𝐹𝑟𝑜𝑚 𝐶𝑎𝑝𝑡𝑖𝑜𝑛.
○ 𝑼𝒑𝒍𝒐𝒂𝒅 𝑫𝒊𝒓𝒆𝒄𝒕𝒍𝒚 𝑰𝒏 𝒀𝒐𝒖𝒓 𝑪𝒉𝒂𝒏𝒏𝒆𝒍.
○ 𝑼𝒍𝒕𝒓𝒂 𝑭𝒂𝒔𝒕 𝑺𝒑𝒆𝒆𝒅 😁 
○ ʜɪɢʜ-𝒔ᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ & 𝑼𝒑𝒍𝒐𝒂𝒅
○ 𝑨𝒍𝒍 𝑳𝒊𝒏𝒌𝒔 𝑺𝒖𝒑𝒑𝒐𝒓𝒕𝒆𝒅.
○ 𝑷𝒆𝒓𝒎𝒂𝒏𝒆𝒏𝒕  𝑻𝒉𝒖𝒎𝒃𝒏𝒂𝒊𝒍 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 
○ ꜰᴜʟʟ ᴀᴅᴍɪɴ 𝒔ᴜᴘᴘᴏʀᴛ

✨𝑭𝒐𝒓 ᴜᴘɪ ɪᴅ 𝒐𝒓 𝑸𝑹
 𝑫𝒎 : @Spark_Developer

📜 𝑇𝑒𝑟𝑚𝑠 𝑎𝑛𝑑 𝐶𝑜𝑛𝑑𝑖𝑡𝑖𝑜𝑛𝑠: 𝐹𝑜𝑟 𝑓𝑢𝑟𝑡ℎ𝑒𝑟 𝑑𝑒𝑡𝑎𝑖𝑙𝑠 𝑎𝑛𝑑 𝑐𝑜𝑚𝑝𝑙𝑒𝑡𝑒 𝑡𝑒𝑟𝑚𝑠 𝑎𝑛𝑑 𝑐𝑜𝑛𝑑𝑖𝑡𝑖𝑜𝑛𝑠, 𝑝𝑙𝑒𝑎𝑠𝑒 𝑠𝑒𝑛𝑑 /terms.

ᴄʟɪᴄᴋ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /myplan """
    )
    # Buttons for "See Terms" and "Contact"
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📜 See Terms", callback_data="see_terms")],
            [InlineKeyboardButton("💬 Contact Now", url="https://t.me/Spark_Developer")],
        ]
    )
    await callback_query.message.edit_text(plan_text, reply_markup=buttons)


@app.on_callback_query(filters.regex("see_terms"))
async def see_terms(client, callback_query):
    terms_text = (
        "📜 **Terms and Conditions** 📜\n\n"
        "✨ We are not responsible for user deeds, and we do not promote copyrighted content. If any user engages in such activities, it is solely their responsibility.\n"
        "✨ Upon purchase, we do not guarantee the uptime, downtime, or the validity of the plan. __Authorization and banning of users are at our discretion; we reserve the right to ban or authorize users at any time.__\n"
        "✨ Payment to us **__does not guarantee__** authorization for the /batch command. All decisions regarding authorization are made at our discretion and mood.\n"
    )
    # Buttons for "See Plans" and "Contact"
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📋 See Plans", callback_data="see_plan")],
            [InlineKeyboardButton("💬 Contact Now", url="https://t.me/Spark_Developer")],
        ]
    )
    await callback_query.message.edit_text(terms_text, reply_markup=buttons)
    
