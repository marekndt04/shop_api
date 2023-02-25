class MongoDbCollectionMock:
    def __init__(self, mock_db_reposne):
        self.mock_db_response = iter(mock_db_reposne)

    async def find(self):
        print("Returning mocked database response")
        for item in self.mock_db_response:
            yield item
