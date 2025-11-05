#!/usr/bin/python
# -*- coding: utf-8 -*-

DOCUMENTATION = r'''
---
module: hello
short_description: A simple hello world module
version_added: "1.0.3"
description: 
    - This module prints a custom greeting message
    - Can be used as a test or example module
options:
    name:
        description: The name to greet
        required: false
        type: str
        default: world
    greeting:
        description: The greeting to use
        required: false
        type: str
        default: Hello
author:
    - Pedro Bagatin (@pedrobagatin)
'''

EXAMPLES = r'''
# Basic usage
- name: Say hello
  pedrobagatin.hello_world.hello:

# Custom name
- name: Greet someone
  pedrobagatin.hello_world.hello:
    name: John

# Custom greeting and name
- name: Custom greeting
  pedrobagatin.hello_world.hello:
    greeting: Hi
    name: Alice
'''

RETURN = r'''
message:
    description: The output message from the module
    type: str
    returned: always
    sample: 'Hello, world!'
'''

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=False, default='world'),
            greeting=dict(type='str', required=False, default='Hello'),
        ),
        supports_check_mode=True
    )

    name = module.params['name']
    greeting = module.params['greeting']
    
    message = f"{greeting}, {name}!"
    
    result = dict(
        changed=False,
        message=message
    )

    module.exit_json(**result)

if __name__ == '__main__':
    main()
