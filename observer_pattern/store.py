from observable.iphone_observable_impl import IPhoneObservableImpl
from observer.email_alert_observer_impl import EmailAlertObserver
from observer.mobile_alert_observer_impl import MobileAlertObserver

class Store:
    def main():
        iphone_stock_observable = IPhoneObservableImpl()
        observer1 = EmailAlertObserver(observable=iphone_stock_observable, email='first@gmail.com')
        observer2 = EmailAlertObserver(observable=iphone_stock_observable, email='second@gmail.com')
        observer3 = MobileAlertObserver(observable=iphone_stock_observable, user_name='Ayush')

        iphone_stock_observable.add(observer1)
        iphone_stock_observable.add(observer2)
        iphone_stock_observable.add(observer3)

        iphone_stock_observable.set_stock_count(10)
        # iphone_stock_observable.set_stock_count(-10)
        # iphone_stock_observable.set_stock_count(10)
        


Store.main()