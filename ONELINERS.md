# Ansible One-Liners

Try out some of these commands!

Get Ansible variables about this node:

```
ansible -m setup localhost
```

Run `df` on all hosts Ansible knows about:

```
ansible -a "df -h" all
```

Restart the `cron` service (`--become` allows running root commands):
```
ansible -m service -a "name=cron state=restarted" all --become
```
