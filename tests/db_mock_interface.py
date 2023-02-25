class MongoDbCollectionMock:
    def __init__(self, mock_db_reposne=[]):
        self.mock_db_response = iter(mock_db_reposne)

    async def find(self):
        for item in self.mock_db_response:
            yield item

    async def insert_one(self, product):
        pass
