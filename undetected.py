import undetected_chromedriver as uc

def iniciar_webdriver(proxy=None, headless=False, pos="maximizada"):
    options = uc.ChromeOptions()
    options.add_argument("--password-store=basic")
    options.add_argument(r"--user-data-dir=C:\Users\1agui\AppData\Local\Google\Chrome\User Data\Profile 1")
    options.add_experimental_option(
        "prefs",
        {
            "credentialas_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en,es-MX;q=0.9,es-419;q=0.8,es;q=0.7,mi;q=0.6",
        'Referer': 'https://google.com',
        'DNT': '1'
    }
    options.add_argument(f"--user-agent={HEADERS['User-Agent']}")
    options.add_argument(f"--accept-language={HEADERS['Accept-Language']}")
    options.add_argument(f"--referer={HEADERS['Referer']}")
    options.add_argument(f"--dnt={HEADERS['DNT']}")

    if proxy:
        proxy_string = f"--proxy-server={proxy}"
        options.add_argument(proxy_string)

    driver = uc.Chrome(
        options=options,
        headless=headless,
        log_level=3,
    )

    if not headless:
        driver.maximize_window()
        if pos != "maximizada":
            ancho, alto = driver.get_window_size().values()
            if pos == "izquierda":
                driver.set_window_rect(x=0, y=0, width=ancho//2, height=alto)
            elif pos == "derecha":
                driver.set_window_rect(x=ancho//2, y=0, width=ancho//2, height=alto)
    return driver