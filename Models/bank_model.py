class BankModel:
    def __init__(self, bank_id: int, bank_name: str, bank_address: str, bank_swift_code: str):
        self.bank_id = bank_id
        self.bank_name = bank_name
        self.bank_address = bank_address
        self.bank_swift_code = bank_swift_code