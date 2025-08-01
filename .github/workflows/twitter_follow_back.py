import os
import requests

BEARER_TOKEN = os.environ["TWITTER_BEARER_TOKEN"]
USER_ID = os.environ["TWITTER_USER_ID"]
API_BASE = "https://api.twitter.com/2"

def get_followers():
    url = f"{API_BASE}/users/{USER_ID}/followers"
    resp = requests.get(url, headers={"Authorization": f"Bearer {BEARER_TOKEN}"})
    return [f["id"] for f in resp.json().get("data", [])]

def get_following():
    url = f"{API_BASE}/users/{USER_ID}/following"
    resp = requests.get(url, headers={"Authorization": f"Bearer {BEARER_TOKEN}"})
    return [f["id"] for f in resp.json().get("data", [])]

def follow_user(target_id):
    url = f"{API_BASE}/users/{USER_ID}/following"
    resp = requests.post(
        url,
        headers={"Authorization": f"Bearer {BEARER_TOKEN}"},
        json={"target_user_id": target_id}
    )
    print(f"Followed {target_id}: {resp.status_code}, {resp.text}")

def main():
    followers = set(get_followers())
    following = set(get_following())
    to_follow = followers - following
    for uid in to_follow:
        follow_user(uid)

if __name__ == "__main__":
    main()