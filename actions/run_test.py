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

import subprocess
from lib.base_action import BaseAction


class RunTest(BaseAction):
    def __init__(self, config):
        """Creates a new Action given a StackStorm config object (kwargs works too)
        :param config: StackStorm configuration object for the pack
        :returns: a new Action
        """
        super(RunTest, self).__init__(config)

    def run(self, tags_exclude, tags_include, test_path, variables):
        var_arr = self.parse_variables(variables)
        tags_arr = self.parse_tags(tags_exclude, tags_include)

        cmd = [self.exec_path] + var_arr + tags_arr + [test_path]

        result = subprocess.run(cmd, encoding='utf-8', stdout=subprocess.PIPE)
        return_code = result.returncode

        if return_code != 0:
            if result.stderr:
                error = result.stderr
            else:
                error = result.stdout
            raise RuntimeError(error)

        return result.stdout
