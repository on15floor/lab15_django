from datetime import datetime


def build_collection(time_start: str, time_stop: str, price_start: int, price_stop: int) -> dict:
    """Собираем статистику в коллекцию для передачи в шаблон"""
    time_start = datetime.strptime(time_start, '%Y-%m-%d')
    time_stop = datetime.strptime(time_stop, '%Y-%m-%d')
    time_now = datetime.now()

    days_smoking = time_stop - time_start
    days_no_smoking = time_now - time_stop
    price_avg = (price_start + price_stop) / 2
    money_spent = days_smoking.days * price_avg
    money_saved = days_no_smoking.days * price_stop

    return {
        'time_start': time_start.strftime('%Y-%m-%d'),
        'time_stop': time_stop.strftime('%Y-%m-%d'),
        'time_now': time_now.strftime('%Y-%m-%d'),
        'days_smoking': days_smoking.days,
        'days_no_smoking': days_no_smoking.days,
        'price_start': price_start,
        'price_stop': price_stop,
        'price_avg': price_avg,
        'money_spent': money_spent,
        'money_saved': money_saved,
    }
