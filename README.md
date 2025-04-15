# Парсер биржевых данных с MFD.ru

## 📌 Описание
Автоматизированный парсер для сбора данных с сайта [mfd.ru](https://mfd.ru). Собирает актуальную информацию по:
- Котировкам акций
- Объемам торгов
- Изменениям цен
- Ключевым финансовым показателям

## 📊 Пример результатов

![Снимок данных за 2024-05-20](screenshots/sample_output.png)  
*Рис. 1: Данные по акциям (столбцы: тикер, цена, изменение в %)*

### Структура данных
Поле | Описание
-----|---------
Ticker | Тикер ценной бумаги
Last Price | Последняя цена сделки
Change (abs)|  Абсолютное изменение цены
Change (%) | Изменение цены в процентах
Price before closing | Цена перед закрытием предыдущей сессии
Price at opening |  Цена при открытии текущей сессии
Minimum price |   Минимальная цена за сессию
Average overpriced |    Средняя цена
Pieces per day |    Количество лотов за день
Quantity per day | Общий объем сделок в штуках
Rub         | Объем сделок в рублях
Number of transactions per day | Количество сделок за день
## ⚙️ Технические характеристики
- **Язык программирования:** Python 3.11
- **Основные библиотеки:**
  - Selenium 4.9.1
  - Pandas 2.2.3
  - Fake-useragent 2.1.0
- **Режим работы:** headless (без графического интерфейса)
- **Формат данных:** CSV с разделителем "^"

## 🚀 Быстрый старт

### Установка
```bash
git clone https://github.com/yourrepo/mfd-parser.git
cd mfd-parser
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
pip install -r requirements.txt
