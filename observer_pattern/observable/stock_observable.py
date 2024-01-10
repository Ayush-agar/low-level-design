# from observer.

class StockObservable:

    def add(observer):
        raise NotImplementedError()
    
    def delete(observer):
        raise NotImplementedError()
    
    def notify_subscribers():
        raise NotImplementedError()

    def set_stock_count(new_stock):
        raise NotImplementedError()
    
    def get_stock_count():
        raise NotImplementedError()