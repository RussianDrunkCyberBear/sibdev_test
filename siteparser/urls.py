from django.urls import path

from . import views

urlpatterns = [
    path('', views.parse_results)
]



# запуск скрипта парсера в отдельном потоке после загрузки приложения
# незнаю как проверить успешный	запуск приложения, костыль - urls загружется позже остального
import threading
from siteparser.sheduled_parse import sheduledParse

run_sheduled_parse = threading.Thread(target=sheduledParse, args=())
run_sheduled_parse.daemon = True
run_sheduled_parse.start()
