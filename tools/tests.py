import binascii
import unittest
from unittest.mock import patch, mock_open

from django.http import HttpResponse
from django.test import Client
# Create your tests here.
from django.test import TestCase

from community.models import Map
from signup.models import User


class MapTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='nick', password='123')

    def test_map_create(self):
        Map.objects.create(map_name='map', map_url='', user_id=self.user.id)
        maps = Map.objects.filter(user_id=self.user.id)
        self.assertEqual(len(maps), 1)

    def test_map_str(self):
        map = Map.objects.create(map_name='map', map_url='', user_id=self.user.id)
        self.assertEqual(str(map), map.map_name)

    def test_map_field_maxlength(self):
        map = Map.objects.create(map_name='map', map_url='', user_id=self.user.id)
        max_length = map._meta.get_field('map_name').max_length
        self.assertEqual(max_length, 50)
        max_length = map._meta.get_field('map_url').max_length
        self.assertEqual(max_length, 100)

    @unittest.skip("sqlite does not require the field length of char field")
    def test_map_create_failed_with_exceeded_field(self):
        map_name = ['x' for i in range(100)]
        print(map_name)
        map = Map.objects.create(map_name=map_name, map_url='', user_id=self.user.id)
        self.assertEqual(map.map_name, map_name)
        # self.assertRaises()

    def tearDown(self) -> None:
        self.user.delete()


class ToolsViewsTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_index(self):
        c = Client()
        response = c.get('/tool/')
        self.assertEqual(response.status_code, 200)

    @patch('tools.views.render')
    def test_mock_index(self, mock_render):
        c = Client()
        mock_render.return_value = HttpResponse('tools_html')
        response = c.get('/tool/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'tools_html')

    @patch('builtins.open', new_callable=mock_open())
    def test_save_map(self, mock_open_):
        c = Client()
        response = c.post('/tool/save', {
            'map_data': 'PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiIHdpZHRoPSIxMjFweCIgaGVpZ2h0PSI2MXB4IiB2aWV3Qm94PSItMC41IC0wLjUgMTIxIDYxIiBjb250ZW50PSImbHQ7bXhmaWxlIGV0YWc9JnF1b3Q7VGdBR2JKbGNJaGw3a1JuRGFxSDQmcXVvdDsgYWdlbnQ9JnF1b3Q7TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTRfNikgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzgwLjAuMzk4Ny4xMDYgU2FmYXJpLzUzNy4zNiZxdW90OyBtb2RpZmllZD0mcXVvdDsyMDIwLTAyLTE5VDEyOjQ0OjI3LjY1OVomcXVvdDsgaG9zdD0mcXVvdDt0ZXN0LmRyYXcuaW8mcXVvdDsgdmVyc2lvbj0mcXVvdDtARFJBV0lPLVZFUlNJT05AJnF1b3Q7Jmd0OyZsdDtkaWFncmFtIGlkPSZxdW90O3JVdXh2bWFtZE5aMXpyTFhPbF82JnF1b3Q7IG5hbWU9JnF1b3Q7UGFnZS0xJnF1b3Q7Jmd0O2xaUExic0l3RUVXL0prc2t4Nll0V3dvcGZhaWxLcXFRMkpsNGNGdzVHZVFZU1ByMVRZaWRCeXphcmpJK21VZm1YaWRnczdSWUdMNVBYbEdBRGlnUlJjRG1BYVVocGF4NjFLUnN5VjFEcEZIQ3NRNnMxRGM0U0J3OUtBSDVJTkVpYXF2MlF4aGpsa0ZzQjR3Ymc2ZGgyZzcxY09xZVM3Z0NxNWpyYTdwV3dpWU5uZHlRamorQ2tvbWZIQkwzSnVVKzJZRTg0UUpQUGNTaWdNME1vbTJpdEppQnJ0WHp1cnlGNy9NeFpSK2piRU5pU2FmUlJxcFIwK3poUHlYdENnWXkrOWZXbnptWTVmYXJscFFTemJlVnIrZktsZVhHTmczOTBPeXdIZHVuWTFnc1g5YlBiSWU0THFlamJzUDJJM05iZWxVTkhqSUJkVDBKMkwzVVBNOWQzS3BVSDVvNVJ6QVdpZ3M3ZnRrbDdJMWZBS1pnVFZuVnVTN01lK0p1NWNRZFQ1M0RvVTlKZXU3ZU9zYmRwWkp0NTA2NEtuQWIrMk5QU284NjE4L3B2WitIUlQ4PSZsdDsvZGlhZ3JhbSZndDsmbHQ7L214ZmlsZSZndDsiIHN0eWxlPSJiYWNrZ3JvdW5kLWNvbG9yOiByZ2IoMjU1LCAyNTUsIDI1NSk7Ij48ZGVmcy8+PGc+PHJlY3QgeD0iMCIgeT0iMCIgd2lkdGg9IjEyMCIgaGVpZ2h0PSI2MCIgZmlsbD0iI2ZmZmZmZiIgc3Ryb2tlPSIjMDAwMDAwIiBwb2ludGVyLWV2ZW50cz0iYWxsIi8+PGcgZmlsbD0iIzAwMDAwMCIgZm9udC1mYW1pbHk9IkhlbHZldGljYSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMnB4Ij48dGV4dCB4PSI1OS41IiB5PSIzNC41Ij5TdGFydDwvdGV4dD48L2c+PC9nPjwvc3ZnPg==',
            'map_name': 'test_map_name',
            'user_id': '2'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'ok')
        self.assertEqual(response.json()['user_id'], 2)
        self.assertEqual(response.json()['map_url'], '2' + '-' + 'test_map_name'
                         )

    def test_save_map_with_non_base64_img_data(self):
        c = Client()
        with self.assertRaises(binascii.Error) as e:
            response = c.post('/tool/save', {
                'map_data': 'P',
                'map_name': 'test_map_name',
                'user_id': '2'
            })
