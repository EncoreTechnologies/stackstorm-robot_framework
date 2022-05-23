#!/usr/bin/env python
# Copyright 2022 Encore Technologies
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from robot_framework_base_test_case import RobotFrameworkBaseTestCase
from lib.base_action import BaseAction

__all__ = [
    'BaseActionTestCase'
]


class BaseActionTestCase(RobotFrameworkBaseTestCase):
    __test__ = True
    action_cls = BaseAction

    def test_init(self):
        action = self.get_action_instance({})
        self.assertIsInstance(action, BaseAction)

    def test_parse_variables_none(self):
        action = self.get_action_instance({})

        test_variables = None
        expected_result = []

        result = action.parse_variables(test_variables)
        self.assertEqual(result, expected_result)

    def test_parse_variables(self):
        action = self.get_action_instance({})

        test_variables = {'key1': 'value1', 'key2': 'value2'}
        expected_result = ['-v', 'key1: value1', '-v', 'key2: value2']

        result = action.parse_variables(test_variables)
        self.assertEqual(result, expected_result)

    def test_parse_tags_none(self):
        action = self.get_action_instance({})

        test_exclude = None
        test_include = None
        expected_result = []

        result = action.parse_tags(test_exclude, test_include)
        self.assertEqual(result, expected_result)

    def test_parse_tags_both(self):
        action = self.get_action_instance({})

        test_exclude = ['skip']
        test_include = ['run_me', 'run_me_too']
        expected_result = ['-i', 'run_me', '-i', 'run_me_too', '-e', 'skip']

        result = action.parse_tags(test_exclude, test_include)
        self.assertEqual(result, expected_result)

    def test_run(self):
        action = self.get_action_instance({})

        with self.assertRaises(RuntimeError):
            action.run()
