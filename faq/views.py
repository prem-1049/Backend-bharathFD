from django.core.cache import cache
from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get("lang", "en")
        cache_key = f"faqs_{lang}"
        cached_data = cache.get(cache_key)

        if not cached_data:
            faqs = FAQ.objects.all()
            data = [
                {
                    "question": faq.get_translated_question(lang),
                    "answer": faq.get_translated_answer(lang),
                }
                for faq in faqs
            ]
            cache.set(cache_key, data, timeout=60 * 15)  # Cache for 15 minutes
            return data
        return cached_data