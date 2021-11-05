import os.path

from tests.base import ApiBase


class TestApi(ApiBase):

    def test_create_segment(self):
        segment_id = self.create_segment()
        segment_id_list = self.get_segments()
        assert segment_id in segment_id_list
        self.delete_segment(segment_id)

    def test_delete_segment(self):
        segment_id = self.create_segment()
        self.delete_segment(segment_id)
        segment_id_list = self.get_segments()
        assert segment_id not in segment_id_list

    def test_create_campaign(self, repo_root):
        campaign_id = self.create_campaign(os.path.join(repo_root, 'files/test.jpg'))
        campaign_id_list = self.get_campaigns()
        assert campaign_id in campaign_id_list
        self.delete_campaign(campaign_id)
