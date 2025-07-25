import httpx

proxy = [
    "113.204.79.230:9091",
    "193.95.53.131:8077",
    "51.79.99.237:4502",
    "57.129.81.201:8080",
    "31.12.75.215:80",
    "185.162.228.90:80",
    "185.162.229.128:80",
    "172.67.181.240:80",
    "188.114.97.181:80",
    "141.101.120.185:80",
    "45.85.119.254:80",
    "160.153.0.8:80",
    "23.227.39.90:80",
    "23.237.210.82:80",
    "185.176.24.215:80",
    "45.194.53.164:80",
    "46.254.92.157:80",
]

for i in proxy:
    try:
        with httpx.Client(proxy=f"http://{str(i.replace('	', ':'))}", timeout=10) as client:
            r = client.get("https://api.openai.com/v1/models", headers={"Authorization": "Bearer YOUR_KEY"})
            print("Прокси работает!" if r.status_code == 200 else "Прокси не работает с OpenAI")
            print(f"http://{str(i.replace('	', ':'))}")
    except Exception as e:
        print(f"Ошибка: {e}")