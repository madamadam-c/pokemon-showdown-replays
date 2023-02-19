from datetime import datetime
import math
def hide_full_damage(log: list):
    for i, line in enumerate(log):
        if any(word in line for word in ("|damage|", "|-damage|", "|-heal|", "|switch|")):
            damage = line.split("|")[4] if "|switch|" in line else line.split("|")[3] 
            if damage == "0 fnt":
                continue
            damage = damage.split(" ")[0]

            hp = math.ceil(int(damage.split("/")[0]) / int(damage.split("/")[1]) * 100)
            line = line.replace(damage, f"{hp}/100")
            log[i] = line

    return log
            

def get_unix_timestamp(timestamp: str):
    timestamp = " ".join(timestamp.split(" ")[:5])
    timestamp = datetime.strptime(timestamp, "%a %b %d %Y %H:%M:%S")
    return int(timestamp.timestamp())
