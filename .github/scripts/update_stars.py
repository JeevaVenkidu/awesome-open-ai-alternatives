import requests
import re

# Tools with GitHub repos
tools = {
    "Perplexica": "ItzCrazyKns/Perplexica",
    "AnythingLLM": "Mintplex-Labs/anything-llm",
    "Open Notebook": "lfnovo/open-notebook",
    "ComfyUI": "comfyanonymous/ComfyUI",
    "Tortoise TTS": "neonbjb/tortoise-tts",
}

README = "README.md"

def get_stars(repo):
    url = f"https://api.github.com/repos/{repo}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()["stargazers_count"]
    return None

with open(README, "r", encoding="utf-8") as f:
    content = f.read()

for name, repo in tools.items():
    stars = get_stars(repo)
    if stars:
        # replace star count in table (format: ⭐ xxxx)
        content = re.sub(rf"(\*\*{name}\*\*.*?\|) ⭐ \d+[kM]?", rf"\1 ⭐ {stars}", content)

with open(README, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ README updated with latest stars")
