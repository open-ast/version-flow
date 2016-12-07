import unittest
from version_flow.version import Version


class VersionGenerationTest(unittest.TestCase):

    def test_version_generation_correct(self):
        self.assertEqual(
            Version((0,0,1), branch='develop', build_id=123).generate(), '0.0.1.dev123')
        self.assertEqual(
            Version((1,0,0), branch='release/1.0.0/12', build_id=5467).generate(), '1.0.0rc5467')
        self.assertEqual(
            Version((1,0,0), branch='master', build_id=6600, tag='v.1.0.0').generate(), '1.0.0')
        self.assertEqual(
            Version((1,0,0), branch='master', build_id=6609).generate(), '1.0.0.post6609')
        self.assertEqual(
            Version((1,2,3), branch='feature/UBR-111', build_id=78, tag='ubr-feature-0').generate(), '1.2.3.dev78')
