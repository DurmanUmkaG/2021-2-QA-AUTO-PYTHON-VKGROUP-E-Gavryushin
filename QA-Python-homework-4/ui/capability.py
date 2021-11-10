def capability_select(apk_path):
    capability = {
        'platformName': 'Android',
        'platformVersion': '10',
        'automationName': 'Appium',
        'appPackage': 'ru.mail.search.electroscope',
        'appActivity': 'ru.mail.search.electroscope.ui.activity.AssistantActivity',
        'app': apk_path,
        'orientation': 'PORTRAIT',
        'autoGrantPermissions': 'true'
    }

    return capability
