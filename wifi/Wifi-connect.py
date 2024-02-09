import pywifi
import time

def connect_to_wifi(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # انتخاب رابط شبکه Wi-Fi

    iface.disconnect()  # قطع اتصال از هر شبکه‌ای که ممکن است متصل باشید

    time.sleep(1)  # انتظار 1 ثانیه برای قطع اتصال

    profile = pywifi.Profile()  # ساخت یک پروفایل جدید برای شبکه Wi-Fi
    profile.ssid = ssid  # تنظیم نام شبکه Wi-Fi
    profile.auth = pywifi.const.AUTH_ALG_OPEN  # تنظیم الگوریتم احراز هویت (مثلاً WPA2)
    profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)  # تنظیم نوع احراز هویت (مثلاً WPA2-PSK)
    profile.cipher = pywifi.const.CIPHER_TYPE_CCMP  # تنظیم نوع رمزگذاری (مثلاً AES)

    profile.key = password  # تنظیم رمز عبور شبکه Wi-Fi

    iface.remove_all_network_profiles()  # حذف همه پروفایل‌های شبکه‌های قبلی
    tmp_profile = iface.add_network_profile(profile)  # اضافه کردن پروفایل جدید

    iface.connect(tmp_profile)  # اتصال به شبکه Wi-Fi با استفاده از پروفایل جدید

    time.sleep(5)  # انتظار 5 ثانیه برای اتصال

    if iface.status() == pywifi.const.IFACE_CONNECTED:  # چک کردن وضعیت اتصال
        print("Connected to", ssid)
    else:
        print("Connection to", ssid, "failed")

# استفاده از تابع برای اتصال به شبکه Wi-Fi با نام و رمز عبور مشخص
connect_to_wifi("WifiX", "Password")
