from Models.account_model import AccountModel
from datetime import date

class CardModel:
    def __init__(self, card_id: int, account: AccountModel, card_number: str, card_type: str, expiry_date: date, status: str, cvv: str):
        self.card_id = card_id
        self.account = account
        self.card_number = card_number
        self.card_type = card_type
        self.expiry_date = expiry_date
        self.status = status
        self.cvv = cvv