{"filter":false,"title":"test_app.py","tooltip":"/todo/test_app.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":9,"column":66},"action":"insert","lines":["rom django.apps import apps","from django.test import TestCase","from .apps import TodoConfig","","","class TestTodoConfig(TestCase):","","    def test_app(self):","        self.assertEqual(\"todo\", TodoConfig.name)","        self.assertEqual(\"todo\", apps.get_app_config(\"todo\").name)"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":66},"end":{"row":9,"column":66},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":19,"mode":"ace/mode/python"}},"timestamp":1583587142785,"hash":"8e821cba3dc7686e32ed66d4c86d996949d7427e"}