# Payments.py

import yookassa

yookassa.domain.common.amount
yookassa.domain.common.currency

class Payments:
    def __init__(self, shop_id, api_key):
        self.shop_id = shop_id
        self.api_key = api_key
        self.client = yookassa.Client(self.api_key)
    
    def generate_unique_payment_id(self):
        # Здесь добавьте код для генерации уникального ID платежа
        pass
    
    def create_payment(self, amount, currency, description):
        payment_id = self.generate_unique_payment_id()
        
        payment = yookassa.Payment.create({
            'amount': {
                'value': str(amount),
                'currency': currency,
            },
            'confirmation': {
                'type': 'redirect',
                'return_url': 'https://your-return-url.com',
            },
            'capture': True,
            'description': description,
            'metadata': {
                'order_id': payment_id,
            },
        }, self.shop_id)
        
        return payment
