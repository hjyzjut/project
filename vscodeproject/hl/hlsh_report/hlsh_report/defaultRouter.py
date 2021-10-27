class DefaultRouter(object):
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'admin' \
           or app_label == 'auth' \
           or app_label == 'staticfiles' \
           or app_label == 'sessions' \
           or app_label == 'messages' \
           or app_label == 'contenttypes':
            return db == 'default'
        return None