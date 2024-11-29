import os
import requests

def get_recently_played_games_with_images(api_key, steam_id, count=3):
    """
    Fetch the most recently played games for a Steam user, including game images.
    """
    url = "https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/"
    params = {"key": api_key, "steamid": steam_id, "count": count}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if 'response' in data and 'games' in data['response']:
            games = data['response']['games']
            return [
                {
                    "name": game["name"],
                    "playtime_2weeks": game["playtime_2weeks"],
                    "image_url": f"https://cdn.cloudflare.steamstatic.com/steam/apps/{game['appid']}/header.jpg",
                    "store_url": f"https://store.steampowered.com/app/{game['appid']}/"
                }
                for game in games
            ]
        else:
            return "No recently played games found or insufficient permissions."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Fetch credentials from environment variables
    API_KEY = os.getenv("STEAM_API_KEY")
    STEAM_ID = os.getenv("STEAM_USER_ID")

    if not API_KEY or not STEAM_ID:
        print("Steam API key and user ID must be set as environment variables.")
    else:
        recent_games = get_recently_played_games_with_images(API_KEY, STEAM_ID)

        if isinstance(recent_games, list) and recent_games:
            # Prepare the markdown content for a table
            markdown_content = """

# Hi, I'm Ozgur Ozbek

**A computer engineer interested in building tools and interacting with games.**

[![Soft](https://skillicons.dev/icons?i=py,js,ts,dotnet,,react,tailwind,html,css,threejs,bootstrap,jquery,,ai,ps,flask,nextjs,nodejs,fastapi,sqlite,postman,graphql,git,,svg,latex,md,regex,figma,materialui,powershell,githubactions,bash,azure,docker,github,heroku,replit,,selenium,vscode,discord,bots,unity,arduino)](https://skillicons.dev)

You'll find a collection of my public products, scripts, or code repositories here. Almost all of my work or commissioned repositories are private. The remaining are either playground materials or small projects. If you have a suggestion or there is something you would like to see me work on in the future, drop an issue **[here](https://github.com/ozgurozbek/ozgurozbek/issues)**!

You should definitely [check out my D&D5E Quest Idea Generator](https://xeculus.pythonanywhere.com/)! It has generated over a million prompts and is used by 100000+ individuals!

[![GitHub Streak](https://streak-stats.demolab.com?user=ozgurozbek&theme=github-dark-blue&mode=weekly&hide_current_streak=true)](https://git.io/streak-stats)

## Contributed Repositories

1. **[PINCE](https://github.com/ozgurozbek-merges/PINCE)**
1. **[XoooX](https://github.com/ozgurozbek-merges/XoooX)**

You can see all my public contributions [here](https://github.com/ozgurozbek-merges).

### Private Repositories

I worked for [Toyota TM&S](https://www.linkedin.com/company/toyotaturkeymarketingandsales/), [Unico Studio](https://www.linkedin.com/company/unico-studio/) and [Inveon](https://www.linkedin.com/company/inveon/) - [Devends](https://www.linkedin.com/company/devends/about/). Unfortunately, those organizations are private, therefore I can't provide organization repositories.

## To my players

* [You should be visiting this link for D&D content](https://ozgurozbek.github.io/teothe)

* [You should be here for Ishibako](https://ozgurozbek.github.io/ishibako/download.html), Ishibako is a small puzzle game that uses pickup-rotate mechanics in a tile-based environment inspired by the original Japanese game Sokoban. Ishibako is still in active development.

* [You should click this for Truth or Drink](https://ozgurozbek.github.io/truthordrink/truthordrink.html). Truth or Drink is a web-scraped question spammer that can output adult content. I have similar one-page party games like it, such as [Never Have I Ever](https://ozgurozbek.github.io/truthordrink/neverhaveiever.html) or [You Laugh You Drink](https://ozgurozbek.github.io/truthordrink/youlaughyoudrink.html).

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=ozgurozbek&layout=compact&langs_count=4&hide=html&size_weight=0.5&count_weight=0.75)

## You can also find more of my work at

* [D&D5E Quest Idea Generator](https://xeculus.pythonanywhere.com/)
* [My website](https://xeculus.wordpress.com/)
* [Cubelue, a casual Android game](https://play.google.com/store/apps/details?id=com.OzgurOzbek.Cubelue&hl=en_US&gl=US)
* [RPG Gibberish Generator](https://replit.com/@ozgurozbek/RPGGibberishGenerator#main.py)
* [Codingame Contribution #1](https://www.codingame.com/contribute/view/45417ee569f7763981a0876ba491bffde4e5)
* [Codingame Contribution #2](https://www.codingame.com/contribute/view/49981fecba44952abebcfbeb65898292d32c)

## Some of my academic writing

* [Literature Review on Applications of Fuzzy Logic Modelling Approaches to Cognitive Radio Systems](https://ozgurozbek.github.io/assets/index-files/bachelorsLiteratureReview.pdf)
* [Unity3D LDRP Online Strategy Game with Mirror Networking and MiniMax AI thesis paper](https://ozgurozbek.github.io/assets/index-files/bachelorsThesis.pdf)

"""

            markdown_content += "## Recently Played Games\n\n"

            # Create the headers dynamically based on the number of games
            game_names_header = "| " + " | ".join([game["name"] for game in recent_games]) + " |"
            markdown_content += game_names_header + "\n"
            markdown_content += "|-" + "-|-".join(["-" * len(game["name"]) for game in recent_games]) + "-|\n"

            # Create rows for images and playtimes
            game_links = " | ".join([f"[![{game['name']}]({game['image_url']})]({game['store_url']})" for game in recent_games])
            game_playtimes = " | ".join([f"{game['playtime_2weeks']} mins" for game in recent_games])

            # Add rows to the markdown content
            markdown_content += f"| {game_links} |\n"
            markdown_content += f"| {game_playtimes} |\n"

            # Write to markdown file
            with open("README.md", "w") as file:
                file.write(markdown_content)

            print("Markdown file created.")
        else:
            print("No recently played games found or insufficient permissions.")
