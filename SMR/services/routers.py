import requests
from utils.sellers import get_sellers
from utils.scoring import score_sellers

def route_query(query: str):
    sellers = get_sellers(query)
    scored = score_sellers(sellers)
    return sorted(scored, key=lambda x: x['score'], reverse=True)
