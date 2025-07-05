def score_sellers(sellers):
    scored_list = []
    for s in sellers:
        score = 0
        score += (5 - s['price'] / 100)  # lower price = higher score
        score += s['rating']
        if s['stock']:
            score += 2
        scored_list.append({**s, "score": round(score, 2)})
    return scored_list
