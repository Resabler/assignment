import redis
from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
#writing the custom middleware logic
class req(MiddlewareMixin):
    request='req_count'
    reset='reset_count'
    def process(request,self):
        if request.method=='POST':
            cache.set(self.KEY, 0)
            req_count = cache.get(self.KEY, 0)
        
        # Increment the request count and save it back to cache
            req_count += 1
            cache.set(self.REQUEST_COUNT_KEY, req_count)
 
       