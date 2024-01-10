from observer.notification_alert_observer_impl import NotificationAlertObserver
from observable.stock_observable import StockObservable

class EmailAlertObserver(NotificationAlertObserver):
    observable: StockObservable
    email: str
    def __init__(self, observable, email):
        self.observable = observable
        self.email = email

    def update(self):
        self.send_email(self.email, "product in stock, hurry up!")
    
    def send_email(self, email, msg):
        print(f"Send email to {email} with message {msg}")
        # send the actual email to end user