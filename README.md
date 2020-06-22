# Анализ значений ОЕЕ с помощью Telegram
## Описание
Определение узкого места в производстве является достаточно сложной проблемой само по себе. Крупным производителям требуется вести контроль в реальном времения за своими производственными площадкам.
Для решение этой задачи был разработан инструмент, позволяющий контролировать параметры эффективности системы (ОЕЕ) без необходимотси использования ПК.
Особенностью системы является возможность контроля незапланированных остановок, что способствует определению узкого места в работе производственной линии.
## Принцип работы
Система выполняет:
- сбор данных, как OPC UA Client с ПЛК
- Анализ данных
- Оперативное информирования об аварийных состояниях в группу Telegram
- Составляение и отправка мини отчетов раз в производственную смену
- Логгирование
## Настройка
### Paramms OPC
```url = "opc.tcp://10.4.37.2:4840 (You OPC UA Server)"
client = Client(url)
### Paramms Telegram
CHANNEL_NAME1 = '@YouChannel_0'
apihelper.proxy = {'https': 'https://login:pass@ip:port'}
CHANNEL_NAME_PET1 = '@YouChannel_1'
CHANNEL_NAME_PET2 = '@YouChannel_2'
CHANNEL_NAME_PET3 = '@YouChannel_3'
token = 'YouToken'
```
