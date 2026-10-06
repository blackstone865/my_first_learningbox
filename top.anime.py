import requests
url = "https://api.jikan.moe/v4/top/anime"
params = {"limit": 50}

print("正在获取 MyAnimeList 高分动漫排行榜...")

try:
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        anime_list = data["data"]
        print(f"\n成功获取 {len(anime_list)} 部动漫！\n")
        print("-" * 60)
        for idx, anime in enumerate(anime_list, 1):
            title = anime.get("title", "未知标题")
            score = anime.get("score", "暂无评分")
            episodes = anime.get("episodes", "未知")
            anime_type = anime.get("type", "未知类型")
            print(f"#{idx}  {title}")
            print(f"   类型: {anime_type} | 集数: {episodes} | 评分: {score}")
            print("-" * 60)
    else:
        print(f"请求失败，状态码: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"网络请求出错: {e}")