import unittest

from DataBridge import DataBridge

class Test_DataBridge(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getting_api_key_secrets(self):
        secrets = DataBridge.getApiKeySecrets()
        self.assertIsNotNone(secrets, "No CoinMarketCap API Key found")

    def test_adding_to_cryptos_of_interest(self):
        cryptos_1 = DataBridge.getCryptosOfInterest()
        ticker = "abc123"
        DataBridge.addToCryptosOfInterest(ticker)
        cryptos_2 = DataBridge.getCryptosOfInterest()
        self.assertIsNot(cryptos_1, cryptos_2, "cryptos_of_interest is same before AND after the new ticker was added")

    
    
    # def test_WhenAddedZeroItems_ListIsEmpty(self):
    #     self.assertEqual(0, self.List.count())

    

if (__name__ == '__main__'):
	unittest.main()
