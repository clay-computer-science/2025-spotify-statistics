import os
import requests
import urllib.parse
from flask import Flask, redirect, request, session, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Needed for session

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPE = "user-top-read"

@app.route("/")
def login():
    query = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "scope": SCOPE,
        "redirect_uri": REDIRECT_URI
    }
    url_args = urllib.parse.urlencode(query)
    auth_url = f"https://accounts.spotify.com/authorize?{url_args}"
    return f'<a href="{auth_url}">Log in with Spotify</a>'

@app.route("/callback")
def callback():
    code = request.args.get("code")
    token_url = "https://accounts.spotify.com/api/token"
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    response = requests.post(token_url, data=payload)
    response_data = response.json()
    access_token = response_data.get("access_token")
    session["access_token"] = access_token
    return redirect("/top-artist")

@app.route("/top-artist")
def top_artist():
    access_token = session.get("access_token")
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    top_url = "https://api.spotify.com/v1/me/top/artists?limit=1"
    res = requests.get(top_url, headers=headers)
    data = res.json()
    if "items" in data and len(data["items"]) > 0:
        artist = data["items"][0]["name"]
        return f"<h1>Your Top Artist is: {artist}</h1>"
    else:
        return "Couldn't fetch top artist."

if __name__ == "__main__":
    app.run(debug=True)