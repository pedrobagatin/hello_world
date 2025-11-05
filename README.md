# Ansible Collection: pedrobagatin.hello_world

A tiny example Ansible collection that provides a single demonstration module, `hello`, which prints a greeting message.

## Contents

- plugins/modules/hello.py — a simple module that returns a greeting message.

## Requirements

- Ansible: >= 2.9.10 (see `meta/runtime.yml`)

## Installation

Install from Galaxy (when published):

```bash
ansible-galaxy collection install pedrobagatin.hello_world
```

## Module: hello

FQCN: `pedrobagatin.hello_world.hello`

Short description: A simple hello world module that returns a greeting message.

Parameters

- `name` (string, optional) — The name to greet. Default: `world`.
- `greeting` (string, optional) — The greeting to use. Default: `Hello`.

Return

- `message` (string) — The resulting greeting, e.g. `"Hello, world!"`.

Example playbook

```yaml
- hosts: localhost
	gather_facts: false
	tasks:
		- name: Say hello with the collection module
			pedrobagatin.hello_world.hello:
				name: Alice
				greeting: Hi
			register: hello_result

		- name: Show module output
			debug:
				var: hello_result.message
```

You can run the example locally with:

```bash
ansible-playbook -i localhost, -c local playbook.yml
```

Notes on usage

- Use the fully-qualified collection name to avoid ambiguity: `pedrobagatin.hello_world.hello`.

Testing

There is no automated test harness included in this tiny example. To manually test the module:

1. Install the collection locally as described in "Installation".
2. Run the example playbook above.

Publishing to Galaxy

1. Ensure `galaxy.yml` and `meta` metadata are filled out.
2. Build the collection:

```bash
ansible-galaxy collection build
```

3. Publish using your Galaxy credentials (or use the web UI):

```bash
ansible-galaxy collection publish <path-to-tarball>
```

Author:

Pedro Bagatin (pedrobagatin@yahoo.com.br)
