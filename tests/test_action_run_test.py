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

import mock
import subprocess
from robot_framework_base_test_case import RobotFrameworkBaseTestCase
from run_test import RunTest

__all__ = [
    'RunTestTestCase'
]


class RunTestTestCase(RobotFrameworkBaseTestCase):
    __test__ = True
    action_cls = RunTest

    def test_init(self):
        action = self.get_action_instance({})
        self.assertIsInstance(action, RunTest)

    @mock.patch('run_test.subprocess.run')
    def test_run_no_vars_no_tags(self, mock_run):
        action = self.get_action_instance({})

        test_path = '/path/to/test.robot'
        test_variables = None
        test_include = None
        test_exclude = None
        expected_cmd = ['robot', '/path/to/test.robot']

        mock_result = mock.Mock(stdout='success', returncode=0)
        mock_run.return_value = mock_result

        expected_result = 'success'
        result = action.run(test_exclude, test_include, test_path, test_variables)

        mock_run.assert_called_with(expected_cmd, encoding='utf-8',
                                    stdout=subprocess.PIPE)
        self.assertEqual(result, expected_result)

    @mock.patch('run_test.subprocess.run')
    def	test_run_vars_tags(self, mock_run):
        action = self.get_action_instance({})

        test_path = '/path/to/test.robot'
        test_variables = {'key1': 'value1', 'key2': 'value2'}
        test_include = ['run_me', 'run_me_too']
        test_exclude = ['skip']

        expected_cmd = ['robot', '-v', 'key1: value1', '-v', 'key2: value2', '-i', 'run_me',
                        '-i', 'run_me_too', '-e', 'skip', '/path/to/test.robot']

        mock_result = mock.Mock(stdout='success', returncode=0)
        mock_run.return_value = mock_result

        expected_result = 'success'
        result = action.run(test_exclude, test_include, test_path, test_variables)

        mock_run.assert_called_with(expected_cmd, encoding='utf-8',
                                    stdout=subprocess.PIPE)
        self.assertEqual(result, expected_result)

    @mock.patch('run_test.subprocess.run')
    def	test_run_error_stdout(self, mock_run):
        action = self.get_action_instance({})

        test_path = '/path/to/test.robot'
        test_variables = None
        test_include = None
        test_exclude = None
        expected_cmd = ['robot', '/path/to/test.robot']

        mock_result = mock.Mock(stderr=None, stdout='stdout_error', returncode=1)
        mock_run.return_value = mock_result

        with self.assertRaisesRegex(RuntimeError, 'stdout_error'):
            action.run(test_exclude, test_include, test_path, test_variables)

        mock_run.assert_called_with(expected_cmd, encoding='utf-8',
                                    stdout=subprocess.PIPE)

    @mock.patch('run_test.subprocess.run')
    def test_run_error_stderr(self, mock_run):
        action = self.get_action_instance({})

        test_path = '/path/to/test.robot'
        test_variables = None
        test_include = None
        test_exclude = None
        expected_cmd = ['robot', '/path/to/test.robot']

        mock_result = mock.Mock(stderr='stderr_error', returncode=1)
        mock_run.return_value =	mock_result

        with self.assertRaisesRegex(RuntimeError, 'stderr_error'):
            action.run(test_exclude, test_include, test_path, test_variables)

        mock_run.assert_called_with(expected_cmd, encoding='utf-8',
                                    stdout=subprocess.PIPE)
