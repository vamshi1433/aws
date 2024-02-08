import random
import time
import requests
from datetime import datetime, timedelta

# Chat ID of your Telegram channel or group
CHAT_ID = '-1002062164933'
# Your bot token
BOT_TOKEN = '6878057144:AAEsLaCw0BqFFOmG0d6SerkVV46vf6qToAc'

def get_current_period():
    # Get the current time in UTC
    utc_time = datetime.utcnow()

    # Convert UTC time to IST
    ist_time = utc_time + timedelta(hours=5, minutes=30)

    # Check if it's 12 AM (00:00:00), if so, reset the period to 0000
    if ist_time.hour == 0 and ist_time.minute == 0 and ist_time.second == 0:
        return f"{ist_time.year}{str(ist_time.month).zfill(2)}{str(ist_time.day).zfill(2)}0000"

    # Extract year, month, day, and period from IST time
    current_year = ist_time.year
    current_month = str(ist_time.month).zfill(2)
    current_day = str(ist_time.day).zfill(2)
    current_period = str((ist_time.hour * 60 + ist_time.minute) + 1).zfill(4)

    return f"{current_year}{current_month}{current_day}01{current_period}"

def send_to_telegram(message):
    # Add HTML tags for bold formatting
    formatted_message = f"<b>{message}</b>"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        'chat_id': CHAT_ID,
        'text': formatted_message,
        'parse_mode': 'HTML'  # Specify HTML parsing mode
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Message sent successfully to Telegram.")
    else:
        print("Failed to send message to Telegram.")

def run_game():
    # Run the game until period 1140 is reached
    for _ in range(1140):
        current_period = get_current_period()
        current_time = datetime.now().strftime("%H:%M:%S")
        color = random.choice(['<b>RED❤️ ❤️</b>', '<b>GREEN💚💚</b>'])

        message = (
            f"<b>➡️ BDG- GAME BIG DATA PREDICTION</b>\n\n"
            f"<b>➡️ SERVER: \"WINGO 1 MINUTES\"</b>\n"
            f"<b>👉 CURRENT PERIOD NUMBER: {current_period}</b>\n"
            f"<b>✅ BET ON COLOR: {color} </b>\n"
            f"<b>🔹 ALWAYS FOLLOW TRIPLE INVESTMENT METHOD TO SUCH AS FOLLOW PREDICTION 1X 3X 9X 27X 81X 243X 🔹</b>\n"
            f"<b>✅ TO REPORT ANY ERROR, PLEASE CONTACT YOUR SUPERIOR, YOUR FEEDBACK MATTERS TO US‼️</b>\n"
            f"<b>_ THANK YOU FOR BEING A BDG GAME MEMBER❤️</b>"
        )

        send_to_telegram(message)

        # Wait for 1 minute before the next iteration
        time.sleep(60)

if __name__ == "__main__":
    run_game()

