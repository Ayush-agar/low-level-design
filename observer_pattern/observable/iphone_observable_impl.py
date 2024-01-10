from observable.stock_observable import StockObservable
from observer.notification_alert_observer_impl import NotificationAlertObserver
from typing import List

class IPhoneObservableImpl(StockObservable):

    observer_list : List[NotificationAlertObserver] = []
    stock_count = 0

    def add(self, observer: NotificationAlertObserver):
        self.observer_list.append(observer)

    def delete(self, observer: NotificationAlertObserver):
        self.observer_list.remove(observer)
    
    def notify_subscribers(self):
        for ob in self.observer_list:
            ob.update()
    
    def set_stock_count(self, new_stock):
        if self.stock_count == 0:
            self.notify_subscribers()
        self.stock_count += new_stock
    
    def get_stock_count(self):
        return self.stock_count
