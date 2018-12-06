from django.test import TestCase

from django.urls import reverse

from minerals.models import Mineral


# Create your tests here.
class MineralViewsTest(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name = "Stevenite",
            category = "Techdegree Student",
            )
        self.mineral2 = Mineral.objects.create(
            name = "Stonite",
            category = "rock",
            )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_details_view(self):
        resp = self.client.get(reverse('minerals:details',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])