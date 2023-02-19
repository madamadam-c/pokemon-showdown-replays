from datetime import datetime
import math
def create_replay_object(log: dict, show_full_damage: bool = False):
    if not all(key in log for key in ('p1', 'p2', 'log', 'inputLog', 'roomid', 'format')):
        raise ValueError("Invalid log object")
    
    if not show_full_damage:
        log['log'] = hide_full_damage(log['log'])

    log_as_string = "\n".join(log['log'])[:-1]

    timestamp = get_unix_timestamp(log['timestamp'])
    
    private = {
        'private': log['roomid'].count('-') == 3,
        'password': "" if not log['roomid'].count('-') == 3 else log['roomid'].split('-')[3]
    }

    format = log['format']

    if "|tier|" in log_as_string:
        format = log_as_string.split("|tier|")[1].split("\n")[0]

    return {
        'id': log['roomid'],
        'format': format,
        'p1': log['p1'],
        'p2': log['p2'],
        'log': log_as_string,
        'inputLog': log['inputLog'],
        'timestamp': timestamp,
        'private': private
    }
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
