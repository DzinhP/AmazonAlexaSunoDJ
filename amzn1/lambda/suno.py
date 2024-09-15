import httpx
import time


def starttask(topic, tag):
    resp = httpx.post("https://studio-api.suno.ai/api/external/generate/", json={
        "topic": topic,
        "tags": tag
    },
        headers={"authorization": "Bearer IJINRGk7moduVetDSfZGofg5MuluAWqE",
                 'accept': "/",
                 'origin': 'https://suno.com',
                 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
                 })
        
    return resp.json()["id"]


def check(idstuff):
    resp = httpx.get(f"https://studio-api.suno.ai/api/feed/v2/?ids={idstuff}", headers={
                     "authorization": "Bearer IJINRGk7moduVetDSfZGofg5MuluAWqE"}).json()
    return (resp["clips"], resp["clips"][0]["status"])


def getmusic(idstuff):
    print(idstuff)
    clips, status = check(idstuff)
    while status != "complete":
        clips, status = check(idstuff)
        time.sleep(5)
    return clips[0]["audio_url"]



