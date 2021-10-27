# 数据分库处理

from django.db import models


class Router(object):
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'report':
            return db == 'fill_in'
        return None

    def db_for_write(self, model, **hints):
        print(model._meta)
        if model._meta.app_label == 'report':
            return 'fill_apps'
        return None

    def db_for_read(self, model, **hints):
        # 配置每个app使用那个数据库读
        if model._meta.app_label == 'report':
            return 'fill_apps'
        return None
