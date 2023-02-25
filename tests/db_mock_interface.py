from pymongo.errors import DuplicateKeyError


class MongoDbCollectionMock:
    def __init__(self, mock_db_reposne=[], duplicate_key_error=False):
        self.mock_db_response = iter(mock_db_reposne)
        self.duplicate_key_error = duplicate_key_error

    async def find(self):
        for item in self.mock_db_response:
            yield item

    async def insert_one(self, product):
        if self.duplicate_key_error:
            raise DuplicateKeyError(error="duplicate key error")
        else:
            pass
