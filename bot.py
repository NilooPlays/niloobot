from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

import os

TOKEN = os.environ["TOKEN"]

def main_menu():
    keyboard = [
        [
            InlineKeyboardButton("📊 اطلاعات", callback_data="info"),
            InlineKeyboardButton("⚙️ تنظیمات", callback_data="settings")
        ],
        [
            InlineKeyboardButton("📢 کانال", callback_data="channel"),
            InlineKeyboardButton("👤 پروفایل", callback_data="profile")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 پنل اصلی\n\n👇 یکی از گزینه‌ها رو انتخاب کن:",
        reply_markup=main_menu()
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        keyboard = [
            [InlineKeyboardButton("🔙 برگشت", callback_data="back")]
        ]

        await query.edit_message_text(
            "📊 اطلاعات\n\n"
            "🤖 وضعیت ربات: فعال ✅\n"
            "🟢 اتصال: برقرار\n"
            "⚡ سیستم: Online",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "settings":
        keyboard = [
            [InlineKeyboardButton("🔔 اعلان‌ها", callback_data="notifications")],
            [InlineKeyboardButton("🌐 زبان", callback_data="language")],
            [InlineKeyboardButton("🔙 برگشت", callback_data="back")]
        ]

        await query.edit_message_text(
            "⚙️ تنظیمات\n\nیک گزینه را انتخاب کن:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "notifications":
        keyboard = [
            [InlineKeyboardButton("🔙 برگشت به تنظیمات", callback_data="settings")]
        ]

        await query.edit_message_text(
            "🔔 اعلان‌ها\n\n"
            "وضعیت اعلان‌ها: فعال ✅",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "language":
        keyboard = [
            [InlineKeyboardButton("🇮🇷 فارسی", callback_data="persian")],
            [InlineKeyboardButton("🇬🇧 English", callback_data="english")],
            [InlineKeyboardButton("🔙 برگشت به تنظیمات", callback_data="settings")]
        ]

        await query.edit_message_text(
            "🌐 انتخاب زبان:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "persian":
        keyboard = [
            [InlineKeyboardButton("🔙 برگشت", callback_data="language")]
        ]

        await query.edit_message_text(
            "🇮🇷 زبان فارسی انتخاب شد.",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "english":
        keyboard = [
            [InlineKeyboardButton("🔙 Back", callback_data="language")]
        ]

        await query.edit_message_text(
            "🇬🇧 English selected.",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "channel":
        keyboard = [
            [InlineKeyboardButton("🔙 برگشت", callback_data="back")]
        ]

        await query.edit_message_text(
            "📢 کانال\n\nاینجا می‌تونیم لینک و اطلاعات کانالت رو قرار بدیم.",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "profile":
        user = query.from_user

        keyboard = [
            [InlineKeyboardButton("🔙 برگشت", callback_data="back")]
        ]

        await query.edit_message_text(
            f"👤 پروفایل\n\n"
            f"نام: {user.first_name}\n"
            f"آیدی عددی: {user.id}\n"
            f"Username: @{user.username if user.username else 'ندارد'}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "back":
        await query.edit_message_text(
            "🤖 پنل اصلی\n\n👇 یکی از گزینه‌ها رو انتخاب کن:",
            reply_markup=main_menu()
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("ربات روشن شد...")
import os

app.run_webhook(
    listen="0.0.0.0",
    port=int(os.environ.get("PORT", 10000)),
    webhook_url=os.environ.get("WEBHOOK_URL"),
)