from observer.notification_alert_observer_impl import NotificationAlertObserver
from observable.stock_observable import StockObservable

class MobileAlertObserver(NotificationAlertObserver):
    observable: StockObservable
    user_name: str
    def __init__(self, observable, user_name):
        self.observable = observable
        self.user_name = user_name

    def update(self):
        self.send_mobile_msg(self.user_name, "product in stock, hurry up!")
    
    def send_mobile_msg(self, user_name, msg):
        print(f"Send message to {user_name} with text {msg}")
        # send the actual message to end user's mobile