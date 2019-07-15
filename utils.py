import io
import yaml

def add_user_to_yaml(user, json):
    raise NotImplementedError

def add_policy_to_all_users(policy, users, user_yaml):
    """ useryaml tools"""
    with open(user_yaml, 'r') as stream:
        data_loaded = yaml.safe_load(stream)

    policies = data_loaded['rbac']['policies']

    found = False
    for pl in policies:
        if pl["id"] == policy:
            found = True

    if not found:
        print("ERROR: no {} resource!!!".format(policy))
        return

    for user in users:
        if user in data_loaded['users']:
            policies = data_loaded['users'][user]['policies']
            if not isinstance(policies, list):
                policies = [policies]
            if policy not in policies:
                policies.append(policy)
        else:
            print("WARNING: {} does not exist".format(user))

        # Write YAML file
    with io.open(user_yaml, 'w', encoding='utf8') as outfile:
        yaml.dump(data_loaded, outfile, default_flow_style=False, allow_unicode=True)

    print("End!!!")
