import os
from dotenv import load_dotenv

# Load env variables if running locally
load_dotenv()

# TELEGRAM - otomatis bersihkan spasi
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "").strip()
raw_user_id = os.getenv("ALLOWED_USER_ID", "0").strip()
try:
    ALLOWED_USER_ID = int(raw_user_id)
except ValueError:
    ALLOWED_USER_ID = 0

# SUPABASE
SUPABASE_URL = os.getenv("SUPABASE_URL", "").strip().rstrip("/")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY", "").strip()

# GOOGLE SHEETS
GOOGLE_CREDENTIALS_JSON = os.getenv("GOOGLE_CREDENTIALS_JSON", "").strip()
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID", "").strip()

# APP CONFIG
TIMEZONE = "Asia/Jakarta"
