from rest_framework.response import Response
from api.models.hero import HeroSection

class HeroPageMixin:
    """
    Mixin that automatically attaches hero block to the top-level response.
    Usage:
        - Set `hero_page` on your viewset, e.g. hero_page = "about"
        - Works only for list() responses
    """

    hero_page = None  # override in each viewset

    def get_hero_data(self):
        if not self.hero_page:
            return None
        hero = HeroSection.objects.filter(page=self.hero_page).first()
        if not hero:
            return None
        return {
            "page": hero.page,
            "headline": hero.headline,
            "subheadline": hero.subheadline
        }

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        hero_data = self.get_hero_data()
        return Response({
            "hero": hero_data,
            "data": response.data
        })
