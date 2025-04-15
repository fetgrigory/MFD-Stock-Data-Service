# Парсер биржевых данных с MFD.ru

![Логотип MFD](https://example.com/mfd_logo.png)

## 📌 Описание
Автоматизированный парсер для сбора данных с сайта [mfd.ru](https://mfd.ru). Собирает актуальную информацию по:
- Котировкам акций
- Объемам торгов
- Изменениям цен
- Ключевым финансовым показателям

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
