def get_product_fit_vote_message(data):
    if 'vote' in data and 'product' in data:
        return {
            'vote': data['vote'],
            'product': data['product']
        }
    return None
