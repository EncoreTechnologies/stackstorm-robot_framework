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

import yaml
from st2tests.base import BaseActionTestCase


class RobotFrameworkBaseTestCase(BaseActionTestCase):
    __test__ = False

    def setUp(self):
        super(RobotFrameworkBaseTestCase, self).setUp()
        self._config_good = self.load_yaml('config_good.yaml')
        self._config_blank = self.load_yaml('config_blank.yaml')

    def tearDown(self):
        super(RobotFrameworkBaseTestCase, self).tearDown()

    def load_yaml(self, filename):
        return yaml.safe_load(self.get_fixture_content(filename))

    @property
    def config_good(self):
        return self._config_good

    @property
    def config_blank(self):
        return self._config_blank
