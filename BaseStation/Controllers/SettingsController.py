from PySide import QtCore


class SettingsController(QtCore.QObject):

    DEFAULTS = {
        'expo': 1.5,
        'control': 0,
        'axis': 0,
        'invert': False
    }

    def __init__(self, parent):
        super(SettingsController, self).__init__(parent)
        self.settings = QtCore.QSettings()

    def get(self, key):
        if self.settings.contains(key):
            return self.settings.value(key)
        else:
            token = key.split('/')[-1]
            if token in DEFAULTS:
                default = DEFAULTS[token]
                self.settings.setValue(key, default)
                return default
            else:
                return None

    def set(self, key, value):
        return self.settings.setValue(key, value)
