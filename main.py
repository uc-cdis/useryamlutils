from utils import add_policy_to_all_users

ALL_DEV_USERS = [
    "abbygeorge@uchicago.edu",
    "aprokh@uchicago.edu",
    "atharvar@uchicago.edu",
    "avantol@uchicago.edu",
    "dgrantkeane@uchicago.edu",
    "diw@uchicago.edu",
    "dmiller15@uchicago.edu",
    "emalinowski@uchicago.edu",
    "fantix@uchicago.edu",
    "fauzi@uchicago.edu",
    "fitz@uchicago.edu",
    "giangbui@uchicago.edu",
    "mlukowski@uchicago.edu",
    "mshao1@uchicago.edu",
    "mikeabreu@uchicago.edu",
    "qshu@uchicago.edu",
    "reubenonrye@uchicago.edu",
    "ribeyre@uchicago.edu",
    "rudyardrichter@uchicago.edu",
    "thanhnd@uchicago.edu",
    "vzpgb@uchicago.edu",
    "kuangx@uchicago.edu",
    "yajingt@uchicago.edu",
    "zgowani@uchicago.edu",
    "zlchitty@uchicago.edu"]

ALL_BIO_USERS = [
    "cgmeyer@uchicago.edu",
    "fan1@uchicago.edu",
    "yilinxu@uchicago.edu",
]

ALL_COMMONS = ["accountprod",
               "anvil",
               "bpa",
               "canine",
               "cvb",
               "dcfqa",
               "dcp",
               "dev",
               "edc",
               "genomel",
               "kfqa",
               "ncicrdcdemo",
               "ndh",
               "qa",
               "stagingdatastage",
               "vadcprod"]

def add_policy_for_all_dev_in_all_commons(policy):

    root = "/Users/giangbui/Projects/commons-users/users"

    for common in ALL_COMMONS:
        add_policy_to_all_users(policy, ALL_DEV_USERS, root + "/" + common + "/user.yaml")


def remove_user_from_all_commons(user):
    raise NotImplementedError


def add_user_to_common(user, user_yaml, json_block):
    raise NotImplementedError


def main():
    add_policy_for_all_dev_in_all_commons("prometheus")


if __name__ == "__main__":
    main()
