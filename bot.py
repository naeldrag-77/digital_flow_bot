import logging
import os
from flask import Flask
from threading import Thread
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# Logging setup
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# --- Render ዌብ ሰርቨር ክፍት እንዲሆን የሚያደርግ ትንሽዬ Flask ኮድ ---
app = Flask('')

@app.route('/')
def home():
    return "Digital Flow Bot is running 24/7! 🚀"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
# -----------------------------------------------------------

# የይዘት ጽሁፎች
DEF_TEXT = (
    "🤔📱 **1. ዲጂታል ማስታወቂያ ምን ማለት ነው?**\n\n"
    "ዲጂታል ማስታወቂያ ማለት ምርትዎን፣ ሱቅዎን ወይም አገልግሎትዎን በኢንተርኔት፣ በማህበራዊ ሚዲያ (ቲክቶክ፣ ፌስቡክ፣ ቴሌግራም) እና በሌሎች የዲጂታል መድረኮች አማካኝነት ለታለመው ደንበኛ በቀጥታ ማድረስ ማለት ነው።\n\n"
    "💡 **I now ይገባናል** አብዛኛው ነጋዴዎች ስራቸውን በ social ሚዲያ ያስተዋውቃሉ ግን ኮንስስተንሲ ያለው **AI automated + editing video** በማሰራት ጊዜያችሁን እና ወጪያችሁን ቆጥቡ!"
)

BENEFIT_TEXT = (
    "📲 **2. ዲጂታል ማስታወቂያ ለንግድ ምን ጥቅም አለው?**\n\n"
    "• **ሰፊ ተደራሽነት፦** የምንሰራውን የዲጂታል ማስታወቂያዎች ቪዲዮዎች በ social ሚዲያ በአጭር ጊዜ ለብዙ ሰው ለማሳየት በጣም ይጠቅማል።\n"
    "• **ውጤታማ እና ቆጣቢ፦** ከባህላዊ ማስታወቂያዎች በበለጠ በርካሽ ዋጋ የላቀ ውጤት እና እውቅናን ያስገኛል።\n"
    "• **ፈጣን ሽያጭ እና እውቅና፦** ንግድዎ በዕለታዊ ተጠቃሚዎች ዘንድ በፍጥነት እንዲታወቅ እና ተመራጭ እንዲሆን ይረዳል።\n"
    "• **የተሻለ አገልግሎት፦** እጅግ ጥራት ያላቸውን ማስታወቂያ ስለምንሰራ ንግዳችሁ በደንበኞች ዘንድ ተወዳጅነት ይኖረዋል"
)

PRICE_TEXT = (
    "💰 **4. የዲጂታል ማስታወቂያ ዋጋ ዝርዝር**\n\n"
    "ማስታወቂያዎቻችን እንደ ጥራታቸው እና እንደ ርዝመታቸው የሚወሰኑ ሲሆን፤ ብዙ ለሚያሰሩ ልዩ ቅናሾች አሉን!\n\n"
    "🔹 **Normal ፖኬጅ:** 1 ቪዲዮ = **500 ብር**\n"
    "   *(High Quality + Beast Editing)*\n\n"
    "🔸 **Premium ፖኬጅ:** 1 ቪዲዮ = **700 ብር**\n"
    "   *(Very High Quality 2K + Amazing Edits)*\n\n"
    "⭐ **VIP ፖኬጅ:** 1 ቪዲዮ = **1,000 ብር**\n"
    "   *(Pro Quality 4K + High Editing + ከሶሻል ሚዲያዎ ጋር የሚገናኝ ዌብሳይት)*\n\n"
    "────────────────\n"
    "⚠️ **ማሳሰቢያ:** ብዙ ቪዲዮ የምታሰሩ ትልቅ ቅናሽ አለው❗️\n"
    "🔱 **VIP ማስታወቂያ** የምታሰሩ VIP Channelችን መቀላቀል ትችላላችሁ እንዲሁም የንግድ website ይሰራላችኋል❗️\n\n"
    "• የማስታወቂያ ቪዲዮ ማሰራት የምትፈልጉ ነክታችሁ አናግሩን 👉 **@natismc**\n"
    "📞 ለበለጠ መረጃ እና ለምክክር ደውሉ ☎️ **0980572122**"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    welcome_message = (
        f"ሰላም {user.first_name}!\n\n"
        "**Digital Flow Bot — የንግድዎ ዲጂታል ማስተዋወቂያ ማዕከል!**\n\n"
        "ሰላም የተከበራችሁ የንግድ ባለቤቶች እና ጀማሪ ፈጣሪዎች! ምርትዎን ወይም አገልግሎትዎን ለሰፊው ማህበረሰብ ለማድረስ እንዲሁም ሽያጭዎን በከፍተኛ ደረጃ ለማሳደግ Digital Flow Bot ሙሉ መረጃውን ይነግራችኋል።\n\n"
        "በዋንኝነት የDigital ማስታወቂያ የምንሰጣቸውን አገልግሎቶች እና ዝርዝር መረጃዎች ከታች ይመልከቱ፦"
    )
    
    keyboard = [
        [
            InlineKeyboardButton("🤔📱 1. ዲጂታል ማስታወቂያ ምንድን ነው?", callback_data="def"),
            InlineKeyboardButton("📲 2. ለንግድ ያለው ጥቅም", callback_data="benefit"),
        ],
        [
            InlineKeyboardButton("🎬 3. ቪዲዮ ናሙና (Sample)", callback_data="sample"),
            InlineKeyboardButton("💰 4. የዋጋ ዝርዝር", callback_data="price"),
        ],
        [
            InlineKeyboardButton("📞 አግኙን / ማዘዣ (@natismc)", callback_data="contact"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.message:
        await update.message.reply_text(welcome_message, reply_markup=reply_markup, parse_mode="Markdown")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    chat_id = query.message.chat_id
    back_keyboard = [[InlineKeyboardButton("🔙 ወደ ዋናው ምናሌ (Main Menu)", callback_data="back_to_start")]]
    reply_markup = InlineKeyboardMarkup(back_keyboard)
    
    if query.data == "def":
        await query.edit_message_text(text=DEF_TEXT, reply_markup=reply_markup, parse_mode="Markdown")
    elif query.data == "benefit":
        await query.edit_message_text(text=BENEFIT_TEXT, reply_markup=reply_markup, parse_mode="Markdown")
    elif query.data == "sample":
        sample_keyboard = [
            [InlineKeyboardButton("🎬 ቪዲዮ ናሙና 1", callback_data="vid_1")],
            [InlineKeyboardButton("🎬 ቪዲዮ ናሙና 2", callback_data="vid_2")],
            [InlineKeyboardButton("🎬 ቪዲዮ ናሙና 3", callback_data="vid_3")],
            [InlineKeyboardButton("🔙 ወደ ዋናው ምናሌ (Main Menu)", callback_data="back_to_start")]
        ]
        sample_text = (
            "🎬 **3. የቪዲዮ ናሙናዎች (Samples)**\n\n"
            "ከሰራናቸው የ digital ማስታወቂያዎች ውስጥ አንዱን መርጠው ይመልከቱ 👇👇\n\n"
            "• ለማዘዝ 👉 @natismc\n"
            "📞 0980572122"
        )
        await query.edit_message_text(text=sample_text, reply_markup=InlineKeyboardMarkup(sample_keyboard), parse_mode="Markdown")

    elif query.data in ["vid_1", "vid_2", "vid_3"]:
        vid_back_keyboard = [[InlineKeyboardButton("🔙 ወደ ዋናው ምናሌ (Main Menu)", callback_data="back_to_start")]]
        
        video_urls = {
            "vid_1": "https://raw.githubusercontent.com/naeldrag-77/digital_flow_bot/main/lv_0_20261105151932.mp4",
            "vid_2": "https://raw.githubusercontent.com/naeldrag-77/digital_flow_bot/main/lv_0_20261019085003.mp4",
            "vid_3": "https://raw.githubusercontent.com/naeldrag-77/digital_flow_bot/main/lv_0_20261008211700.mp4"
        }
        
        selected_video_url = video_urls[query.data]
        
        # ቪዲዮ ሲላክ የድሮውን ጽሁፍ አጥፍቶ አዲስ ቪዲዮ በምቾት እንዲያሳይ
        try:
            await query.message.delete()
        except:
            pass
            
        await context.bot.send_video(
            chat_id=chat_id,
            video=selected_video_url,
            caption="🎬 የመረጡት የዲጂታል ማስታወቂያ ናሙና!\n\n• ለማዘዝ 👉 @natismc\n📞 0980572122",
            reply_markup=InlineKeyboardMarkup(vid_back_keyboard)
        )

    elif query.data == "price":
        await query.edit_message_text(text=PRICE_TEXT, reply_markup=reply_markup, parse_mode="Markdown")
    elif query.data == "contact":
        contact_text = (
            "📞 **ለማዘዝ እና ለመነጋገር፦**\n\n"
            "• ቴሌግራም አድራሻ፦ **@natismc**\n"
            "• ስልክ ቁጥር፦ `0980572122`\n\n"
            "በቀጥታ በመደወል ወይም በቴሌግራም በማናገር ትዕዛዝዎን ይስጡ!"
        )
        await query.edit_message_text(text=contact_text, reply_markup=reply_markup, parse_mode="Markdown")
    elif query.data == "back_to_start":
        welcome_message = (
            "🏠 **ዋና ምናሌ (Main Menu)**\n\n"
            "**Digital Flow Bot — የንግድዎ ዲጂታል ማስተዋወቂያ ማዕከል!**\n\n"
            "እባክዎ የሚፈልጉትን መረጃ ከታች ባሉት አማራጮች ይምረጡ፦"
        )
        main_keyboard = [
            [
                InlineKeyboardButton("🤔📱 1. ዲጂታል ማስታወቂያ ምንድን ነው?", callback_data="def"),
                InlineKeyboardButton("📲 2. ለንግድ ያለው ጥቅም", callback_data="benefit"),
            ],
            [
                InlineKeyboardButton("🎬 3. ቪዲዮ ናሙና (Sample)", callback_data="sample"),
                InlineKeyboardButton("💰 4. የዋጋ ዝርዝር", callback_data="price"),
            ],
            [
                InlineKeyboardButton("📞 አግኙን / ማዘዣ (@natismc)", callback_data="contact"),
            ]
        ]
        
        # ከቪዲዮ መልዕክት ላይ ሆነን "ወደ ዋናው ምናሌ" ስንነካ ቪዲዮውን አጥፍቶ ዋናውን ሜኑ በጽሁፍ እንዲመልስ
        try:
            await query.message.delete()
            await context.bot.send_message(chat_id=chat_id, text=welcome_message, reply_markup=InlineKeyboardMarkup(main_keyboard), parse_mode="Markdown")
        except:
            await query.edit_message_text(text=welcome_message, reply_markup=InlineKeyboardMarkup(main_keyboard), parse_mode="Markdown")

def main() -> None:
    t = Thread(target=run_flask)
    t.start()

    TOKEN = os.environ.get("BOT_TOKEN")  
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    application.run_polling()

if __name__ == "__main__":
    main()
