# coding:utf-8

import xadmin
from xadmin.views import BaseAdminPlugin, ListAdminView
from django.template import loader


# excel 导入
class ListImportExcelPlugin(BaseAdminPlugin):
    import_excel = False

    # 当返回是True的时候，加载插件
    def init_request(self, *args, **kwargs):
        return bool(self.import_excel)

    # 在top_toolbar加载templates下面的html代码
    def block_top_toolbar(self, context, nodes):
        nodes.append(
            loader.render_to_string('xadmin/excel/model_list.top_toolbar.import.html', context_instance=context))


xadmin.site.register_plugin(ListImportExcelPlugin, ListAdminView)
