# Get virtual numbers and receive sms

### Available countries (use only codes)
```
'Russia': 'RU',
'Ukraine': 'UA'
```

### Available services
```
'Telegram': 'opt29',
'Twitter': 'opt41',
```

## Quick start
```
from getsmsapi inport Simsms

sim_sms = Simsms(
    api_key='your-api-key',
    country='RU',
    service='opt29'  # Telegram
)

number, order_id = sim_sms.get_number()
number, sms = sim_sms.get_code(order_id)
```
