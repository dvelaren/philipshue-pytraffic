import requests


def get_light(ip, token, verify_ssl=False, light_id=None):
    """Get light info from the bridge."""
    url = f"https://{ip}/clip/v2/resource/light"
    if light_id:
        url += f"/{light_id}"
    headers = {"hue-application-key": token}
    response = requests.get(url, headers=headers, verify=verify_ssl)
    return response.json()


def set_light(ip, token, light_id, brightness=100, x=0.2, y=0.2, verify_ssl=False):
    """Set light state on the bridge."""
    url = f"https://{ip}/clip/v2/resource/light/{light_id}"
    headers = {"hue-application-key": token}
    payload = {
        "dimming": {"brightness": brightness},
        "color": {"xy": {"x": x, "y": y}},
        "on": {"on": True},
    }
    response = requests.put(url, headers=headers, json=payload, verify=verify_ssl)
    return response.json()


def switch_light(ip, token, light_id, state, verify_ssl=False):
    """Set light state on the bridge."""
    url = f"https://{ip}/clip/v2/resource/light/{light_id}"
    headers = {"hue-application-key": token}
    payload = {"on": {"on": state}}
    response = requests.put(url, headers=headers, json=payload, verify=verify_ssl)
    return response.json()
