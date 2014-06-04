import importlib
from .environment import Environment


environments = {}
for mod_name in ['simple_arm', 'pendulum', 'music']:
    module = importlib.import_module('explauto.environment.{}'.format(mod_name))
    env = getattr(module, 'environment')
    conf = getattr(module, 'configurations')
    testcases = getattr(module, 'testcases')
    environments[mod_name] = (env, conf, testcases)