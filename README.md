# Robot Framework Integration Pack

This integration pack allows StackStorm to run Robot Framework tests.

This pack works by invoking the robot CLI directly on the StackStorm node.

## Configuration
You may want to specify the path to the robot binary to use.

Copy the example configuration in robot_framework.yaml.example to /opt/stackstorm/configs/robot_framework.yaml and edit as required.

Note: When modifying the configuration in `/opt/stackstorm/configs/` please remember to tell StackStorm to load these new values by running `st2ctl reload --register-configs`

# Actions
* `run_test` - Run the given robot test and show the results

## Examples

#### `run_test` example
```sh
# run robot test with the given variables
st2 run robot_framework.run_test test_path="/root/test.robot" variables='{"var1": "qwerty", "var2": "asdfg"}'
```

#### `run_test`	example with tags
```sh
# run all robot tests with the specified tag and with the given variables
st2 run robot_framework.run_test test_path="/root/test.robot" variables='{"var1": "qwerty"}' tags_include='run_me'
```
