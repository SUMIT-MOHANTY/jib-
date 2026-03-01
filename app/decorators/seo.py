from functools import wraps
from flask import request, current_app, jsonify

def seo_meta(title=None, description=None, og_type='website', twitter_card='summary_large_image'):
    '''Decorator to inject SEO meta tags into API responses'''
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            response = f(*args, **kwargs)
            
            # Handle tuple responses (status, body) or direct returns
            if isinstance(response, tuple):
                data = response[0]
                status_code = response[1]
            else:
                data = response
                status_code = 200
            
            # Build SEO meta object
            site_name = current_app.config.get('SITE_NAME', 'Portfolio API')
            site_url = current_app.config.get('SITE_URL', 'http://localhost:5000')
            og_image = current_app.config.get('OG_IMAGE_URL', '')
            twitter_handle = current_app.config.get('TWITTER_HANDLE', '@portfolio')
            
            # Dynamic title/description from response if not provided
            page_title = title or site_name
            page_desc = description or current_app.config.get('SITE_DESCRIPTION', '')
            
            # Build meta object
            meta = {
                '_meta': {
                    'title': page_title,
                    'description': page_desc,
                    'og_tags': {
                        'og:title': page_title,
                        'og:description': page_desc,
                        'og:type': og_type,
                        'og:url': request.url,
                        'og:image': og_image,
                        'og:site_name': site_name
                    },
                    'twitter_card': {
                        'twitter:card': twitter_card,
                        'twitter:title': page_title,
                        'twitter:description': page_desc,
                        'twitter:image': og_image,
                        'twitter:site': twitter_handle
                    },
                    'canonical_url': request.url
                }
            }
            
            # Merge meta into response
            if isinstance(data, dict):
                data.update(meta)
            else:
                data = {'data': data, **meta}
            
            if isinstance(response, tuple):
                return data, status_code
            return data
        return decorated_function
    return decorator
