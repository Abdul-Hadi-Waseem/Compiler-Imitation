from keywords import keywords_map

def token_val(token):
    
    keywords_map[token] = keywords_map.get(token, len(keywords_map))
    
    return keywords_map[token]
