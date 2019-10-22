import io
import yaml
import re


def add_policy_to_all_users_str(policy, users, user_yaml):
    with open(user_yaml, 'r') as stream:
        lines = stream.readlines()

    for idx, line in enumerate(lines):
        for user in users:
            if user in line:
                if "policies: [" in lines[idx+2] and "admin:" in lines[idx+1]:
                    m = re.search(': \[(.+?)\]', lines[idx+2])
                    if m and policy not in lines[idx+2]:
                        substr = m.group(1)
                        lines[idx+2] = lines[idx+2].replace(substr, substr + ", {}".format(policy))
    with open(user_yaml, 'w') as stream:
        for item in lines:
            stream.write("%s" % item)


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
        print("ERROR: no {} resource for {}".format(policy, user_yaml))
        return

    add_policy_to_all_users_str(policy, users, user_yaml)

    return
    #
    # for user in users:
    #     if user in data_loaded['users']:
    #         policies = data_loaded['users'][user]['policies']
    #         if not isinstance(policies, list):
    #             policies = [policies]
    #         if policy not in policies:
    #             policies.append(policy)
    #     else:
    #         print("WARNING: {} does not exist".format(user))
    #
    #     # Write YAML file
    # with io.open(user_yaml, 'w', encoding='utf8') as outfile:
    #     yaml.dump(data_loaded, outfile, default_flow_style=False, allow_unicode=True)

    print("End!!!")


def add_user_to_yaml(user, common_json, json_block):
    raise NotImplementedError


def remove_user_from_yaml(user, common_json):
    raise NotImplementedError