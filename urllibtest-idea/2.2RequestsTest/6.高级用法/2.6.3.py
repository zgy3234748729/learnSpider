import requests

headers = {
    'Cookie': '_octo=GH1.1.770571435.1658238073; _device_id=5e68ff2b83b5834a46adb1233ae5268f; user_session=eGqPYuUAF2gnyJRWZQ09y9_kp8NGQkpjzF4IbV72F_kMtA9d; __Host-user_session_same_site=eGqPYuUAF2gnyJRWZQ09y9_kp8NGQkpjzF4IbV72F_kMtA9d; logged_in=yes; dotcom_user=zgy3234748729; has_recent_activity=1; color_mode={"color_mode":"auto","light_theme":{"name":"light","color_mode":"light"},"dark_theme":{"name":"dark","color_mode":"dark"}}; preferred_color_mode=light; tz=Etc/GMT-8; _gh_sess=YMcHcMW3gEoYPfBZzm8Ek+JvItbkO9pAuOllQZa5WwWATF47Q3sT0iuHjTHeVBP4qZw0wMkw7/80E0KnG3CT+34YJRJ0KG4W0OjCMtrl5vizp3+K5ILrLj0YdhhFlhvV2Tr7AEs8w/1azOYPQKFbO8eopX6oCZYv/Bf3hp++ZbdAISCR5pQtfJXerva1csLvcHzObfaPjRdhuLXraGZA1h53u6WxSOIuto8Yu0dkPg8rgS6+mYbwaQE7qrDmIIfflqgN4QuYRY/rwZX5yrAzfhnLx44R4RV+h/fCX1fe3OF2z2YrO/qDqiJ27erAkrR+YuyKrQ==--xY6b1TQKaMGHdmk7--M8nO2Jr9is2MBUEdhUti0g=='
}
r = requests.get('https://github.com/', headers=headers)
print(r.text)