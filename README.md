# Block Telegram Spam

Script that uses the Telegram API to automatically report, block and delete spam
messages that only contain a single document.

## Quick start

1. Install dependencies: `pip install -r requirements.txt`
2. Create a `config.ini` file containing your Telegram `api_id` and `api_hash`:

```
[pyrogram]
api_id = 12345
api_hash = 0123456789abcdef0123456789abcdef
```

3. Run the script and log in: `python main.py`
