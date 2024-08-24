from urllib.parse import urlparse

def is_valid_reddit_url(url: str) -> bool:
    try:
        parsed_url =  urlparse(url)
        # Check if the URL is on 'reddit.com' domain
        if parsed_url.netloc not in ['www.reddit.com', 'old.reddit.com']:
            return False
        
        # Split the URL into parts
        path_parts = parsed_url.path.strip('/').split('/')
        
        # Validate URL for Reddit post
        return (
            (len(path_parts) >= 3 and path_parts[0] == 'r' and path_parts[2] == 'comments') or
            (len(path_parts) >= 2 and path_parts[0] == 'comments')
        )
    except Exception as e:
        print(f"Error validating URL: {e}")
        return False