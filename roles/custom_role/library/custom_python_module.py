# Check out this page for more information!
# http://docs.ansible.com/ansible/dev_guide/developing_modules_general.html#common-module-boilerplate

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec = dict(
            state     = dict(default='present', choices=['present', 'absent']),
            name      = dict(required=True),
            enabled   = dict(required=True, type='bool'),
            something = dict(aliases=['whatever'])
        )
    )

    ansible_return = {
        "changed" : true,
        "rc" : 1,
        "ansible_facts" : {

        }
    }

    return ansible_return

if __name__ == '__main__':
    main()