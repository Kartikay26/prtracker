import datetime
import dateutil.parser
import requests
from collections import Counter

PER_PAGE = 100


def fetch_data(repo, max_days, state="all"):
    data = []
    date_now = datetime.datetime.now(datetime.timezone.utc)
    i = 0
    while True:
        i += 1
        url = f"https://api.github.com/repos/{repo}/pulls?state={state}&per_page={PER_PAGE}&page={i}" 
        resp = requests.get(url)
        resp = resp.json()
        added = 0
        for pr in resp:
            last_date = dateutil.parser.parse(pr['created_at'])
            days_since_last = (date_now - last_date).days
            print(f"debug: on page {i}, days: {days_since_last}")
            if days_since_last > max_days:
                break
            else:
                data.append(pr)
                added += 1
        if added != PER_PAGE:
            break
    usernames = [d['user']['login'] for d in data]
    counts = Counter(usernames)
    returned_list = []
    for username, num in counts.most_common():
        returned_list.append({'username': username, 'count': num})
    return returned_list

# musescore/MuseScore
