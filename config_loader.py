import os
import json
from pathlib import Path
from dotenv import load_dotenv

def load_config():
    # Load .env
    load_dotenv()

    # Load default config JSON
    config_path = Path(__file__).parent / "config" / "default.json"
    with open(config_path) as f:
        config = json.load(f)

    # Override with environment variables if present
    config["api"]["client"]["url"] = os.getenv("API_CLIENT_URL", config["api"]["client"]["url"])
    config["api"]["client"]["app_id"] = os.getenv("API_CLIENT_APP_ID", config["api"]["client"]["app_id"])
    config["api"]["client"]["username"] = os.getenv("API_CLIENT_USERNAME", config["api"]["client"]["username"])
    config["api"]["client"]["password"] = os.getenv("API_CLIENT_PASSWORD", config["api"]["client"]["password"])
    config["api"]["points"]["url"] = os.getenv("API_POINTS_URL", config["api"]["points"]["url"])
    config["influx"]["host"] = os.getenv("INFLUX_HOST", config["influx"]["host"])
    config["influx"]["port"] = os.getenv("INFLUX_PORT", config["influx"]["port"])
    config["influx"]["token"] = os.getenv("INFLUX_TOKEN", config["influx"]["token"])
    config["influx"]["org"] = os.getenv("INFLUX_ORG", config["influx"]["org"])
    config["influx"]["bucket"] = os.getenv("INFLUX_BUCKET", config["influx"]["bucket"])
    config["influx"]["measurement"] = os.getenv("INFLUX_MEASUREMENT", config["influx"]["measurement"])

    return config