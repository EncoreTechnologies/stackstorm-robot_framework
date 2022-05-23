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

from st2common.runners.base_action import Action


class BaseAction(Action):
    def __init__(self, config):
        """Creates a new BaseAction given a StackStorm config object (kwargs works too)
        :param config: StackStorm configuration object for the pack
        :returns: a new BaseAction
        """
        super(BaseAction, self).__init__(config)
        self.exec_path = self.config.get('exec_path', 'robot')

    def parse_variables(self, variables):
        """Loop through the hash of variables and return them in string form
        in the format that the robot command is expecting
        :param variables: List of variables to pass to the robot test
        :returns: Array of variables in the form: ["-v", "key1: value1", "-v", "key2: value2"]
        """
        if variables is None:
            return []

        var_arr = []
        for key, value in variables.items():
            var_arr.append('-v')
            var_arr.append(key + ': ' + value)

        return var_arr

    def parse_tags(self, tags_exclude, tags_include):
        """Loop through the hash of tags to include or exclude in a test run
        in the format that the robot command is expecting
        :param tags_exclude: Select test cases not to run by tag
        :param tags_include: Select tests to run by tag
        :returns: Array of variables in the form: ["-i", "tag1", "-i", "tag2", "-e", "tag3"]
        """
        include = []
        if tags_include is not None:
            for tag in tags_include:
                include.append('-i')
                include.append(tag)

        exclude = []
        if tags_exclude is not None:
            for	tag in tags_exclude:
                exclude.append('-e')
                exclude.append(tag)

        return include + exclude

    # The following function is required for unit tests
    def run(self, **kwargs):
        raise RuntimeError("run() not implemented")

