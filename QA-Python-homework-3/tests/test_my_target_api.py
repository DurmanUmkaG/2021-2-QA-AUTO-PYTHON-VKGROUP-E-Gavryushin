from tests.base import ApiBase


class TestApi(ApiBase):

    def test_create_segment(self):
        segment_id = self.create_segment()
        segment_id_list = self.get_segments()
        assert segment_id in segment_id_list
        self.delete_segment(segment_id)
