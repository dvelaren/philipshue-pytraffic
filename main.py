import os
import time
from dotenv import load_dotenv
from utils import get_light, switch_light, set_light

load_dotenv()

HUE_IP = os.getenv("HUE_IP")
HUE_TOKEN = os.getenv("HUE_TOKEN")
LIGHT_ID = os.getenv("LIGHT_ID") or "225988fd-be25-4243-adea-afb330778bec"

if __name__ == "__main__":
    while True:
        # Red Light
        set_light(HUE_IP, HUE_TOKEN, LIGHT_ID, brightness=100, x=0.8, y=0.3)
        time.sleep(4)
        # Green Light
        set_light(HUE_IP, HUE_TOKEN, LIGHT_ID, brightness=100, x=0.3, y=0.6)
        time.sleep(3)
        # Blue Light
        set_light(HUE_IP, HUE_TOKEN, LIGHT_ID, brightness=100, x=0.7, y=0.7)
        time.sleep(1)
